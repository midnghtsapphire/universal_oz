"""
Task Type Detection
Analyzes prompts to determine the best task category
"""

import re
from typing import Dict, List

# Keywords for each task type
TASK_KEYWORDS = {
    "content_generation": [
        "write", "blog", "article", "content", "seo", "marketing", "social media",
        "copywriting", "email", "newsletter", "post", "caption", "description",
        "product description", "landing page", "ad copy", "press release"
    ],
    "code_generation": [
        "code", "program", "function", "script", "debug", "fix", "implement",
        "python", "javascript", "java", "c++", "sql", "api", "algorithm",
        "refactor", "optimize", "test", "unit test", "class", "method"
    ],
    "data_analysis": [
        "analyze", "data", "statistics", "chart", "graph", "visualization",
        "csv", "excel", "dataframe", "pandas", "numpy", "calculate", "metrics",
        "kpi", "dashboard", "report", "insights", "trends", "correlation"
    ],
    "research": [
        "research", "explain", "what is", "how does", "compare", "difference",
        "history", "background", "overview", "summary", "definition", "concept",
        "theory", "study", "analysis", "review", "literature", "academic"
    ],
    "creative": [
        "story", "creative", "poem", "lyrics", "fiction", "narrative", "character",
        "dialogue", "screenplay", "script", "novel", "short story", "fantasy",
        "sci-fi", "romance", "thriller", "mystery", "adventure"
    ],
    "business": [
        "business plan", "strategy", "market", "competitor", "swot", "roi",
        "revenue", "profit", "growth", "investment", "pitch", "proposal",
        "budget", "forecast", "financial", "sales", "customer", "b2b", "b2c"
    ],
    "technical_writing": [
        "documentation", "technical", "manual", "guide", "tutorial", "how-to",
        "instructions", "specification", "architecture", "design", "api docs",
        "readme", "wiki", "knowledge base", "faq", "troubleshooting"
    ],
    "conversational": [
        "chat", "conversation", "talk", "discuss", "opinion", "advice", "help",
        "recommend", "suggest", "what do you think", "tell me about", "casual"
    ],
    "legal": [
        "legal", "law", "contract", "terms", "policy", "compliance", "regulation",
        "statute", "case law", "precedent", "liability", "rights", "obligations",
        "agreement", "clause", "provision", "jurisdiction"
    ],
    "medical": [
        "medical", "health", "diagnosis", "treatment", "symptoms", "disease",
        "medication", "drug", "patient", "clinical", "healthcare", "pharma",
        "therapy", "condition", "disorder", "syndrome", "pathology"
    ]
}

def detect_task_type(prompt: str) -> str:
    """
    Detect task type based on prompt keywords
    
    Returns the task type with highest keyword match count
    """
    prompt_lower = prompt.lower()
    
    # Count keyword matches for each task type
    scores: Dict[str, int] = {}
    
    for task_type, keywords in TASK_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in prompt_lower:
                # Exact word match gets higher score
                if re.search(r'\b' + re.escape(keyword) + r'\b', prompt_lower):
                    score += 2
                else:
                    score += 1
        scores[task_type] = score
    
    # Get task type with highest score
    if max(scores.values()) == 0:
        # No keywords matched, default to research
        return "research"
    
    best_task = max(scores, key=scores.get)
    return best_task

def get_task_confidence(prompt: str) -> Dict[str, float]:
    """
    Get confidence scores for all task types
    
    Returns dict of task_type: confidence (0-1)
    """
    prompt_lower = prompt.lower()
    scores: Dict[str, int] = {}
    
    for task_type, keywords in TASK_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in prompt_lower:
                if re.search(r'\b' + re.escape(keyword) + r'\b', prompt_lower):
                    score += 2
                else:
                    score += 1
        scores[task_type] = score
    
    # Normalize to 0-1
    total = sum(scores.values())
    if total == 0:
        return {task: 0.0 for task in TASK_KEYWORDS.keys()}
    
    confidences = {task: score / total for task, score in scores.items()}
    return confidences
