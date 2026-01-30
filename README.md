# Universal OZ - Multi-Model AI API

**Query 5 LLMs simultaneously and get unified responses**

Universal OZ is a multi-model AI API that automatically routes your prompts to the top 5 models for each task type, queries them in parallel, and compiles their responses into a single unified document.

---

## 🎯 Features

- ✅ **Auto-Detection:** Automatically detects task type from your prompt
- ✅ **Top 5 Models:** Routes to the best 5 models for each task
- ✅ **Parallel Queries:** Queries all models simultaneously for speed
- ✅ **Unified Response:** Compiles all responses into markdown document
- ✅ **Synthesis:** Optional AI-generated comparison of responses
- ✅ **Cost Tracking:** Estimates total cost per query
- ✅ **10 Task Types:** Content, code, data analysis, research, creative, business, technical writing, conversational, legal, medical

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/midnghtsapphire/universal_oz.git
cd universal_oz
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment

```bash
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

Get your OpenRouter API key at: https://openrouter.ai/keys

### 4. Run Server

```bash
python -m uvicorn api.main:app --reload
```

Server will start at: http://localhost:8000

---

## 📖 Usage

### API Endpoints

#### `POST /query` - Auto-detect task type

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain RAG systems for insurance companies",
    "max_tokens": 2000,
    "temperature": 0.7,
    "include_synthesis": true
  }'
```

#### `POST /query-with-type` - Specify task type

```bash
curl -X POST "http://localhost:8000/query-with-type" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a blog post about AI",
    "task_type": "content_generation",
    "max_tokens": 2000
  }'
```

#### `GET /models` - List all models

```bash
curl "http://localhost:8000/models"
```

#### `GET /task-types` - List supported task types

```bash
curl "http://localhost:8000/task-types"
```

---

## 📊 Task Types & Top 5 Models

### Content Generation
1. Perplexity Sonar - SEO-optimized content
2. Claude 3.5 Sonnet - Long-form professional writing
3. Gemini 2.5 Flash - Fast content generation
4. GPT-4 Turbo - Premium content
5. Mistral Large 2 - Multilingual content

### Code Generation
1. Qwen 2.5 Coder 32B - Code generation, debugging
2. Claude 3.5 Sonnet (Coding) - Complex algorithms
3. DeepSeek Coder - Budget-friendly coding
4. GPT-4 Turbo - Full-stack development
5. Llama 3.3 70B - Open source, fine-tunable

### Data Analysis
1. Claude 3 Opus - Structured data, tables
2. GPT-4 Turbo - Statistical analysis
3. Gemini 2.5 Pro - Large datasets
4. DeepSeek V3 - Budget analysis
5. Claude 3.5 Sonnet - Data interpretation

### Research
1. Perplexity Pro - Real-time web research
2. Claude 3.5 Sonnet - Academic research
3. GPT-4 Turbo - Comprehensive research
4. Gemini 2.5 Pro - Multi-source research
5. Cohere Command R+ - RAG, knowledge base

### Creative Writing
1. Claude 3.5 Sonnet - Creative writing, storytelling
2. GPT-4 Turbo - Fiction, screenplays
3. Character.AI - Character dialogue
4. MiniMax M2-her - Conversation, roleplay
5. Gemini 2.5 Flash - Quick creative ideas

### Business
1. Claude Opus 4.5 - Strategic planning
2. GPT-5 - Deep thinking, systems design
3. Claude 3.5 Sonnet - Business plans
4. GPT-4 Turbo - Market analysis
5. Gemini 2.5 Pro - Financial modeling

### Technical Writing
1. Claude 3.5 Sonnet - Documentation
2. GPT-4 Turbo - API docs, architecture
3. Qwen 2.5 Coder 32B - Code documentation
4. DeepSeek V3 - Technical explanations
5. Gemini 2.5 Flash - Quick reference docs

### Conversational
1. Gemini 2.5 Flash - Fast, natural conversation
2. Claude 3.5 Sonnet - Thoughtful responses
3. Character.AI - Persona consistency
4. MiniMax M2-her - Empathetic conversation
5. GPT-4 Turbo - Complex discussions

### Legal
1. Claude 3 Opus - Legal analysis, contracts
2. Claude Opus 4.5 - Complex legal reasoning
3. OpenAI o1 - Legal research, case law
4. GPT-4 Turbo - Legal documents
5. Cohere Command R+ - Legal knowledge base

### Medical
1. Claude 3 Opus - Medical analysis, HIPAA-aware
2. GPT-4 Turbo - Medical research
3. Claude Opus 4.5 - Complex medical reasoning
4. Gemini 2.5 Pro - Medical literature review
5. Cohere Command R+ - Medical knowledge base

---

## 📝 Response Format

```json
{
  "prompt": "Your original prompt",
  "task_type": "content_generation",
  "models_used": [
    "perplexity/sonar",
    "anthropic/claude-3.5-sonnet",
    "google/gemini-2.5-flash",
    "openai/gpt-4-turbo",
    "mistral/mistral-large-2"
  ],
  "responses": {
    "perplexity/sonar": "Response from Perplexity...",
    "anthropic/claude-3.5-sonnet": "Response from Claude...",
    ...
  },
  "synthesis": "Comparison of all responses...",
  "unified_document": "# Multi-Model Response\n\n...",
  "timestamp": "2026-01-30T12:00:00",
  "total_tokens": 15000,
  "estimated_cost": 0.045
}
```

The `unified_document` field contains a formatted markdown document with:
- All 5 model responses
- Synthesis comparing responses
- Cost summary

---

## 💰 Cost Estimates

| Task Type | Avg Cost per Query | Models Used |
|-----------|-------------------|-------------|
| Content Generation | $0.03-0.05 | Mix of budget + premium |
| Code Generation | $0.02-0.04 | Mostly budget models |
| Data Analysis | $0.05-0.08 | Premium models (Opus, GPT-4) |
| Research | $0.03-0.06 | Mix of budget + premium |
| Creative | $0.02-0.04 | Mix with free models |
| Business | $0.08-0.12 | Premium models (Opus 4.5, GPT-5) |
| Technical Writing | $0.02-0.04 | Mostly budget models |
| Conversational | $0.01-0.03 | Fast, cheap models |
| Legal | $0.08-0.12 | Premium models |
| Medical | $0.08-0.12 | Premium models |

**Note:** Costs are estimates based on average token usage (2000 tokens per response × 5 models = 10,000 tokens total)

---

## 🏗️ Architecture

```
User Prompt
    ↓
Task Detection (keyword analysis)
    ↓
Model Router (get top 5 models)
    ↓
Parallel Queries (5 simultaneous API calls)
    ↓
Response Compiler (markdown document)
    ↓
Unified Response
```

---

## 📁 Project Structure

```
universal_oz/
├── api/
│   ├── __init__.py
│   ├── main.py              # FastAPI server
│   ├── task_detector.py     # Auto-detect task type
│   ├── model_router.py      # Route to top 5 models
│   └── response_compiler.py # Compile responses
├── config/
│   └── (future: user preferences)
├── docs/
│   └── (future: additional documentation)
├── tests/
│   └── (future: unit tests)
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Configuration

### Environment Variables

- `OPENROUTER_API_KEY` - Your OpenRouter API key (required)

### Request Parameters

- `prompt` (required) - Your question or prompt
- `task_type` (optional) - Override auto-detection
- `max_tokens` (optional) - Max tokens per model (default: 2000)
- `temperature` (optional) - Creativity level 0-1 (default: 0.7)
- `include_synthesis` (optional) - Generate synthesis (default: true)

---

## 🚀 Deployment

### Local Development

```bash
python -m uvicorn api.main:app --reload --port 8000
```

### Production (with Gunicorn)

```bash
pip install gunicorn
gunicorn api.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker (future)

```bash
docker build -t universal_oz .
docker run -p 8000:8000 --env-file .env universal_oz
```

---

## 🤝 Use Cases

### 1. Research & Analysis
Get multiple perspectives on complex topics
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain quantum computing for beginners"}'
```

### 2. Code Review
Get code feedback from multiple models
```bash
curl -X POST "http://localhost:8000/query-with-type" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Review this Python function: def calc(x): return x*2",
    "task_type": "code_generation"
  }'
```

### 3. Content Creation
Generate content with multiple perspectives
```bash
curl -X POST "http://localhost:8000/query-with-type" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a blog post about AI ethics",
    "task_type": "content_generation"
  }'
```

### 4. Business Strategy
Get strategic insights from premium models
```bash
curl -X POST "http://localhost:8000/query-with-type" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a go-to-market strategy for a SaaS product",
    "task_type": "business"
  }'
```

---

## 📚 API Documentation

Interactive API docs available at:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 🛠️ Development

### Adding New Models

Edit `api/model_router.py` and add to `MODEL_REGISTRY`:

```python
"your_task_type": [
    {
        "id": "provider/model-name",
        "name": "Model Display Name",
        "cost_per_m": 1.50,
        "specialization": "What it's good at"
    },
    ...
]
```

### Adding New Task Types

1. Add keywords to `api/task_detector.py` in `TASK_KEYWORDS`
2. Add model list to `api/model_router.py` in `MODEL_REGISTRY`

---

## 🐛 Troubleshooting

### Error: "OPENROUTER_API_KEY not found"
- Make sure you created `.env` file from `.env.example`
- Add your OpenRouter API key to `.env`

### Error: "No models found for task type"
- Check that task type exists in `MODEL_REGISTRY`
- Use `/task-types` endpoint to see supported types

### Slow Response Times
- Normal! Querying 5 models takes 5-15 seconds
- Models are queried in parallel for speed
- Consider reducing `max_tokens` for faster responses

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Credits

- **OpenRouter** - Multi-model API access
- **FastAPI** - Web framework
- **Models:** Anthropic, OpenAI, Google, Perplexity, Mistral, Qwen, DeepSeek, and more

---

## 📧 Contact

Created by: [@midnghtsapphire](https://github.com/midnghtsapphire)

---

## 🗺️ Roadmap

- [ ] Web interface for easy querying
- [ ] Save query history
- [ ] Custom model preferences
- [ ] Streaming responses
- [ ] Batch processing
- [ ] Model performance analytics
- [ ] Cost optimization recommendations

---

**Universal OZ** - Get the best of all AI models in one API call 🚀
