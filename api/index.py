from fastapi import FastAPI
from src.agent import ask_agent

app = FastAPI(
    title="Labour Statistics AI Agent",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Labour Statistics AI Agent is running"
    }


@app.get("/ask")
def ask(question: str):
    return ask_agent(question)
