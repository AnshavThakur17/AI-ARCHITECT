from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

from app.routes.analyze import router
from app.routes.history import router as history_router
from app.routes.chat import router as chat_router
from app.database.db import engine, Base

# Create tables on startup if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Architect API"
)

# VERY IMPORTANT

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.include_router(router)
app.include_router(history_router)
app.include_router(chat_router)


@app.get("/", response_class=HTMLResponse)
def home():
    filepath = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return "Error: templates/index.html not found"