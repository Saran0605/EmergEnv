from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Dict, Any
from env import ERCEEnvironment
from models import Action

app = FastAPI(title="ERCE OpenEnv Server")
env_instance = ERCEEnvironment()

class ResetRequest(BaseModel):
    task: str = "easy"

@app.get("/")
def read_root():
    """Root redirect to OpenAPI documentation"""
    return RedirectResponse(url='/docs')

@app.post("/reset")
def reset_env(req: ResetRequest):
    try:
        obs = env_instance.reset(req.task)
        return {"observation": obs.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/step")
def step_env(action: Action):
    try:
        obs, reward, done, info = env_instance.step(action)
        return {
            "observation": obs.model_dump(),
            "reward": reward.model_dump(),
            "done": done,
            "info": info
        }
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/state")
def get_state():
    return env_instance.state().model_dump()

@app.get("/tasks")
def get_tasks():
    return {"tasks": ["easy", "medium", "hard"]}

@app.get("/grader")
def get_grader():
    return {"info": "Grading is fundamentally deterministic, parsing exact logic states against actions using 0-1 metrics boundaries."}

@app.get("/baseline")
def get_baseline():
    return {"info": "To test the reference implementation execute: python baseline.py connecting via REST"}
