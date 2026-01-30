"""
Response Compiler
Compiles multiple model responses into unified markdown document
"""

from typing import List, Dict, Optional
from datetime import datetime

def compile_responses(
    prompt: str,
    task_type: str,
    results: List[Dict],
    include_synthesis: bool = True
) -> Dict:
    """
    Compile multiple model responses into unified document
    
    Args:
        prompt: Original user prompt
        task_type: Detected task type
        results: List of model response dicts
        include_synthesis: Whether to generate synthesis
    
    Returns:
        Dict with 'document', 'synthesis', 'estimated_cost'
    """
    # Filter successful responses
    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]
    
    # Build markdown document
    doc_parts = []
    
    # Header
    doc_parts.append(f"# Multi-Model Response\n")
    doc_parts.append(f"**Prompt:** {prompt}\n")
    doc_parts.append(f"**Task Type:** {task_type}\n")
    doc_parts.append(f"**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    doc_parts.append(f"**Models Queried:** {len(results)}\n")
    doc_parts.append(f"**Successful:** {len(successful)}\n")
    doc_parts.append(f"\n---\n\n")
    
    # Individual responses
    for i, result in enumerate(successful, 1):
        model_name = result["model"].split("/")[-1].replace("-", " ").title()
        doc_parts.append(f"## Response {i}: {model_name}\n\n")
        doc_parts.append(f"**Model ID:** `{result['model']}`\n")
        doc_parts.append(f"**Tokens Used:** {result['tokens']}\n\n")
        doc_parts.append(f"{result['response']}\n\n")
        doc_parts.append(f"---\n\n")
    
    # Failed responses (if any)
    if failed:
        doc_parts.append(f"## ⚠️ Failed Responses\n\n")
        for result in failed:
            doc_parts.append(f"- **{result['model']}:** {result['response']}\n")
        doc_parts.append(f"\n---\n\n")
    
    # Synthesis (optional)
    synthesis = None
    if include_synthesis and len(successful) >= 2:
        synthesis = generate_synthesis(prompt, successful)
        doc_parts.append(f"## 📊 Synthesis\n\n")
        doc_parts.append(f"{synthesis}\n\n")
        doc_parts.append(f"---\n\n")
    
    # Cost summary
    total_tokens = sum(r["tokens"] for r in results)
    estimated_cost = calculate_cost(results)
    
    doc_parts.append(f"## 💰 Cost Summary\n\n")
    doc_parts.append(f"**Total Tokens:** {total_tokens:,}\n")
    doc_parts.append(f"**Estimated Cost:** ${estimated_cost:.4f}\n")
    
    # Combine all parts
    document = "".join(doc_parts)
    
    return {
        "document": document,
        "synthesis": synthesis,
        "estimated_cost": estimated_cost
    }

def generate_synthesis(prompt: str, results: List[Dict]) -> str:
    """
    Generate synthesis comparing all responses
    
    This is a simple rule-based synthesis. For better results,
    you could send all responses to a synthesis model.
    """
    synthesis_parts = []
    
    synthesis_parts.append(f"**Overview:** {len(results)} models provided responses to the prompt.\n\n")
    
    # Common themes
    synthesis_parts.append(f"**Common Themes:**\n")
    synthesis_parts.append(f"- All models addressed the core question\n")
    synthesis_parts.append(f"- Responses varied in depth and approach\n\n")
    
    # Response lengths
    lengths = [(r["model"], len(r["response"])) for r in results]
    longest = max(lengths, key=lambda x: x[1])
    shortest = min(lengths, key=lambda x: x[1])
    
    synthesis_parts.append(f"**Response Lengths:**\n")
    synthesis_parts.append(f"- Longest: {longest[0].split('/')[-1]} ({longest[1]:,} characters)\n")
    synthesis_parts.append(f"- Shortest: {shortest[0].split('/')[-1]} ({shortest[1]:,} characters)\n\n")
    
    # Quality assessment
    synthesis_parts.append(f"**Quality Notes:**\n")
    synthesis_parts.append(f"- Review each response above for accuracy and completeness\n")
    synthesis_parts.append(f"- Consider combining insights from multiple responses\n")
    synthesis_parts.append(f"- Premium models (GPT-4, Claude Opus) typically provide more depth\n\n")
    
    # Recommendation
    synthesis_parts.append(f"**Recommendation:**\n")
    synthesis_parts.append(f"Read all responses and synthesize the best elements from each. ")
    synthesis_parts.append(f"Different models excel at different aspects - combine their strengths.\n")
    
    return "".join(synthesis_parts)

def calculate_cost(results: List[Dict]) -> float:
    """
    Calculate estimated cost based on tokens used
    
    This is a rough estimate. Actual costs vary by model.
    Average cost: ~$3/M tokens
    """
    total_tokens = sum(r["tokens"] for r in results)
    # Rough average: $3 per million tokens
    cost_per_token = 3.0 / 1_000_000
    return total_tokens * cost_per_token
