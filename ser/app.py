from fastapi import FastAPI
from pydantic import BaseModel
from server.env import TrafficMedEnv   # ✅ FIXED import

app = FastAPI()
env = TrafficMedEnv()

# Request model
class Action(BaseModel):
    action: int

# Reset environment
@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

# Take a step
@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action.action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
