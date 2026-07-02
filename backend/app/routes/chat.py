from fastapi import APIRouter
import ollama
from app.models.chat_model import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat_explain(data: ChatRequest):
    system_prompt = f"""
You are a senior distributed systems architect. 
The user is asking a question about a system architecture design you recommended.

Context of the recommended design:
- Original User Prompt: "{data.prompt}"
- Recommended Architecture Components: {data.architecture}
- Recommended Primary Database: {data.database}

Answer the user's question: "{data.question}"

Guidelines:
1. Provide a concise, clear, and direct explanation.
2. Avoid unnecessary engineering jargon. Keep it plain and practical.
3. Be conversational but professional. Focus on explaining the tradeoffs (e.g., why you chose MongoDB over PostgreSQL, or why a queue is helpful).
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": data.question
                }
            ]
        )
        return {"response": response["message"]["content"]}
    except Exception:
        # Fallback explanation if Ollama is down or has connection issues
        q = data.question.lower()
        if "mongo" in q and ("sql" in q or "postgres" in q):
            return {"response": f"I recommended {data.database} because of your application structure. NoSQL/MongoDB excels at storing dynamic schemas (like chat messages or product catalogs) and scaling horizontally, whereas SQL databases are optimized for relational joins and strict ACID compliance."}
        elif "redis" in q or "cache" in q:
            return {"response": "A caching layer (like Redis) stores frequently accessed query results in-memory. This enables sub-millisecond responses and prevents your primary database from being overloaded by duplicate read queries."}
        elif "load balancer" in q or "lb" in q:
            return {"response": "A Load Balancer distributes user requests evenly across multiple backend servers. This prevents any single server from crash-overloading and ensures high availability."}
        elif "queue" in q or "kafka" in q or "rabbitmq" in q:
            return {"response": "A Message Queue decouples heavy write tasks (like processing transactions or sending notifications) asynchronously. This prevents user interface requests from waiting on long database operations."}
        else:
            return {"response": f"Great question. In this design ({', '.join(data.architecture)} with {data.database}), each layer plays a specific role. Component choices are balanced between consistency (SQL), throughput (Queues), and low latency (Redis/CDNs) based on the requirement specs."}
