"""
Universal OZ Multi-Model API
Routes prompts to top 5 models per task type and compiles unified responses
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import asyncio
import aiohttp
import os
from datetime import datetime

from .task_detector import detect_task_type
from .model_router import get_top_models
from .response_compiler import compile_responses

app = FastAPI(
    title="Universal OZ API",
    description="Multi-model AI API that queries top 5 models and compiles responses",
    version="1.0.0"
)

# CORS middleware for web interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class QueryRequest(BaseModel):
    prompt: str
    task_type: Optional[str] = None
    max_tokens: Optional[int] = 2000
    temperature: Optional[float] = 0.7
    include_synthesis: Optional[bool] = True

class QueryResponse(BaseModel):
    prompt: str
    task_type: str
    models_used: List[str]
    responses: Dict[str, str]
    synthesis: Optional[str]
    unified_document: str
    timestamp: str
    total_tokens: int
    estimated_cost: float

# OpenRouter API configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

async def query_model(
    session: aiohttp.ClientSession,
    model_id: str,
    prompt: str,
    max_tokens: int,
    temperature: float
) -> Dict:
    """Query a single model via OpenRouter"""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/midnghtsapphire/universal_oz",
        "X-Title": "Universal OZ API"
    }
    
    payload = {
        "model": model_id,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        async with session.post(OPENROUTER_BASE_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "model": model_id,
                    "response": data["choices"][0]["message"]["content"],
                    "tokens": data["usage"]["total_tokens"],
                    "success": True
                }
            else:
                error_text = await response.text()
                return {
                    "model": model_id,
                    "response": f"Error: {response.status} - {error_text}",
                    "tokens": 0,
                    "success": False
                }
    except Exception as e:
        return {
            "model": model_id,
            "response": f"Error: {str(e)}",
            "tokens": 0,
            "success": False
        }

async def query_multiple_models(
    models: List[Dict],
    prompt: str,
    max_tokens: int,
    temperature: float
) -> List[Dict]:
    """Query multiple models in parallel"""
    async with aiohttp.ClientSession() as session:
        tasks = [
            query_model(session, model["id"], prompt, max_tokens, temperature)
            for model in models
        ]
        results = await asyncio.gather(*tasks)
        return results

@app.get("/")
async def root():
    """API health check"""
    return {
        "status": "online",
        "api": "Universal OZ Multi-Model API",
        "version": "1.0.0",
        "endpoints": ["/query", "/query-with-type", "/models", "/task-types"]
    }

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """
    Main endpoint: Send prompt, get responses from top 5 models
    
    Auto-detects task type and routes to best models
    """
    # Detect task type if not provided
    task_type = request.task_type or detect_task_type(request.prompt)
    
    # Get top 5 models for this task type
    top_models = get_top_models(task_type, limit=5)
    
    if not top_models:
        raise HTTPException(status_code=400, detail=f"No models found for task type: {task_type}")
    
    # Query all models in parallel
    results = await query_multiple_models(
        top_models,
        request.prompt,
        request.max_tokens,
        request.temperature
    )
    
    # Compile responses
    compiled = compile_responses(
        prompt=request.prompt,
        task_type=task_type,
        results=results,
        include_synthesis=request.include_synthesis
    )
    
    return QueryResponse(
        prompt=request.prompt,
        task_type=task_type,
        models_used=[r["model"] for r in results if r["success"]],
        responses={r["model"]: r["response"] for r in results},
        synthesis=compiled["synthesis"],
        unified_document=compiled["document"],
        timestamp=datetime.now().isoformat(),
        total_tokens=sum(r["tokens"] for r in results),
        estimated_cost=compiled["estimated_cost"]
    )

@app.post("/query-with-type", response_model=QueryResponse)
async def query_with_type(request: QueryRequest):
    """
    Query with explicit task type (skips auto-detection)
    """
    if not request.task_type:
        raise HTTPException(status_code=400, detail="task_type is required for this endpoint")
    
    return await query(request)

@app.get("/models")
async def get_models():
    """List all available models organized by task type"""
    from .model_router import MODEL_REGISTRY
    return MODEL_REGISTRY

@app.get("/task-types")
async def get_task_types():
    """List all supported task types"""
    from .model_router import MODEL_REGISTRY
    return {
        "task_types": list(MODEL_REGISTRY.keys()),
        "description": "Use these task types with /query-with-type endpoint"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
