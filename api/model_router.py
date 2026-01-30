"""
Model Router
Maps task types to top 5 models with pricing and specialization info
"""

from typing import List, Dict

# Model registry organized by task type
# Top 5 models for each task, ordered by quality/suitability
MODEL_REGISTRY = {
    "content_generation": [
        {
            "id": "perplexity/sonar",
            "name": "Perplexity Sonar",
            "cost_per_m": 0.20,
            "specialization": "SEO-optimized content, blogs, reviews"
        },
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Long-form content, professional writing"
        },
        {
            "id": "google/gemini-2.5-flash",
            "name": "Gemini 2.5 Flash",
            "cost_per_m": 0.075,
            "specialization": "Fast content generation, social media"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Premium content, complex topics"
        },
        {
            "id": "mistral/mistral-large-2",
            "name": "Mistral Large 2",
            "cost_per_m": 3.00,
            "specialization": "Multilingual content, European market"
        }
    ],
    
    "code_generation": [
        {
            "id": "qwen/qwen-2.5-coder-32b",
            "name": "Qwen 2.5 Coder 32B",
            "cost_per_m": 0.30,
            "specialization": "Code generation, debugging"
        },
        {
            "id": "anthropic/claude-3.5-sonnet:coding",
            "name": "Claude 3.5 Sonnet (Coding)",
            "cost_per_m": 3.00,
            "specialization": "Complex algorithms, architecture"
        },
        {
            "id": "deepseek/coder",
            "name": "DeepSeek Coder",
            "cost_per_m": 0.14,
            "specialization": "Budget-friendly coding"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Full-stack development"
        },
        {
            "id": "meta-llama/llama-3.3-70b",
            "name": "Llama 3.3 70B",
            "cost_per_m": 0.60,
            "specialization": "Open source, fine-tunable"
        }
    ],
    
    "data_analysis": [
        {
            "id": "anthropic/claude-3-opus",
            "name": "Claude 3 Opus",
            "cost_per_m": 15.00,
            "specialization": "Structured data, tables, analysis"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Statistical analysis, insights"
        },
        {
            "id": "google/gemini-2.5-pro",
            "name": "Gemini 2.5 Pro",
            "cost_per_m": 1.25,
            "specialization": "Large datasets, visualization"
        },
        {
            "id": "deepseek/v3",
            "name": "DeepSeek V3",
            "cost_per_m": 0.27,
            "specialization": "Budget analysis, reasoning"
        },
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Data interpretation, reports"
        }
    ],
    
    "research": [
        {
            "id": "perplexity/pro",
            "name": "Perplexity Pro",
            "cost_per_m": 1.00,
            "specialization": "Real-time web research, citations"
        },
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Academic research, synthesis"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Comprehensive research"
        },
        {
            "id": "google/gemini-2.5-pro",
            "name": "Gemini 2.5 Pro",
            "cost_per_m": 1.25,
            "specialization": "Multi-source research"
        },
        {
            "id": "cohere/command-r-plus",
            "name": "Cohere Command R+",
            "cost_per_m": 3.00,
            "specialization": "RAG, knowledge base queries"
        }
    ],
    
    "creative": [
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Creative writing, storytelling"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Fiction, screenplays"
        },
        {
            "id": "character-ai",
            "name": "Character.AI",
            "cost_per_m": 0.00,
            "specialization": "Character dialogue, personas"
        },
        {
            "id": "minimax/m2-her",
            "name": "MiniMax M2-her",
            "cost_per_m": 0.50,
            "specialization": "Conversation, roleplay"
        },
        {
            "id": "google/gemini-2.5-flash",
            "name": "Gemini 2.5 Flash",
            "cost_per_m": 0.075,
            "specialization": "Quick creative ideas"
        }
    ],
    
    "business": [
        {
            "id": "anthropic/claude-opus-4.5",
            "name": "Claude Opus 4.5",
            "cost_per_m": 20.00,
            "specialization": "Strategic planning, complex analysis"
        },
        {
            "id": "openai/gpt-5",
            "name": "GPT-5",
            "cost_per_m": 15.00,
            "specialization": "Deep thinking, systems design"
        },
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Business plans, proposals"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Market analysis, strategy"
        },
        {
            "id": "google/gemini-2.5-pro",
            "name": "Gemini 2.5 Pro",
            "cost_per_m": 1.25,
            "specialization": "Financial modeling"
        }
    ],
    
    "technical_writing": [
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Documentation, technical guides"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "API docs, architecture"
        },
        {
            "id": "qwen/qwen-2.5-coder-32b",
            "name": "Qwen 2.5 Coder 32B",
            "cost_per_m": 0.30,
            "specialization": "Code documentation"
        },
        {
            "id": "deepseek/v3",
            "name": "DeepSeek V3",
            "cost_per_m": 0.27,
            "specialization": "Technical explanations"
        },
        {
            "id": "google/gemini-2.5-flash",
            "name": "Gemini 2.5 Flash",
            "cost_per_m": 0.075,
            "specialization": "Quick reference docs"
        }
    ],
    
    "conversational": [
        {
            "id": "google/gemini-2.5-flash",
            "name": "Gemini 2.5 Flash",
            "cost_per_m": 0.075,
            "specialization": "Fast, natural conversation"
        },
        {
            "id": "anthropic/claude-3.5-sonnet",
            "name": "Claude 3.5 Sonnet",
            "cost_per_m": 3.00,
            "specialization": "Thoughtful, nuanced responses"
        },
        {
            "id": "character-ai",
            "name": "Character.AI",
            "cost_per_m": 0.00,
            "specialization": "Persona consistency"
        },
        {
            "id": "minimax/m2-her",
            "name": "MiniMax M2-her",
            "cost_per_m": 0.50,
            "specialization": "Empathetic conversation"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Complex discussions"
        }
    ],
    
    "legal": [
        {
            "id": "anthropic/claude-3-opus",
            "name": "Claude 3 Opus",
            "cost_per_m": 15.00,
            "specialization": "Legal analysis, contracts"
        },
        {
            "id": "anthropic/claude-opus-4.5",
            "name": "Claude Opus 4.5",
            "cost_per_m": 20.00,
            "specialization": "Complex legal reasoning"
        },
        {
            "id": "openai/o1",
            "name": "OpenAI o1",
            "cost_per_m": 15.00,
            "specialization": "Legal research, case law"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Legal documents"
        },
        {
            "id": "cohere/command-r-plus",
            "name": "Cohere Command R+",
            "cost_per_m": 3.00,
            "specialization": "Legal knowledge base RAG"
        }
    ],
    
    "medical": [
        {
            "id": "anthropic/claude-3-opus",
            "name": "Claude 3 Opus",
            "cost_per_m": 15.00,
            "specialization": "Medical analysis, HIPAA-aware"
        },
        {
            "id": "openai/gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "cost_per_m": 10.00,
            "specialization": "Medical research"
        },
        {
            "id": "anthropic/claude-opus-4.5",
            "name": "Claude Opus 4.5",
            "cost_per_m": 20.00,
            "specialization": "Complex medical reasoning"
        },
        {
            "id": "google/gemini-2.5-pro",
            "name": "Gemini 2.5 Pro",
            "cost_per_m": 1.25,
            "specialization": "Medical literature review"
        },
        {
            "id": "cohere/command-r-plus",
            "name": "Cohere Command R+",
            "cost_per_m": 3.00,
            "specialization": "Medical knowledge base"
        }
    ]
}

def get_top_models(task_type: str, limit: int = 5) -> List[Dict]:
    """
    Get top N models for a given task type
    
    Args:
        task_type: The task category
        limit: Number of models to return (default 5)
    
    Returns:
        List of model dictionaries with id, name, cost, specialization
    """
    models = MODEL_REGISTRY.get(task_type, [])
    return models[:limit]

def get_all_task_types() -> List[str]:
    """Get list of all supported task types"""
    return list(MODEL_REGISTRY.keys())

def get_model_info(model_id: str) -> Dict:
    """Get info for a specific model across all task types"""
    for task_type, models in MODEL_REGISTRY.items():
        for model in models:
            if model["id"] == model_id:
                return {
                    **model,
                    "task_type": task_type
                }
    return None
