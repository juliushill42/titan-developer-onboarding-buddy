from fastapi import FastAPI
from agent import Agent46
app = FastAPI(title="Developer-Onboarding-Buddy")
agent = Agent46()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
