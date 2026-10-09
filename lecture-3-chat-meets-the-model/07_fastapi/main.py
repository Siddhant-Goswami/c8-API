# diagnose() behind a door. Local: uvicorn main:app --reload  ·  Render: uvicorn main:app --host 0.0.0.0 --port $PORT

import os, requests
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

load_dotenv()   # laptop: reads .env · Render: uses dashboard env vars

# input: workflow (text)   output: plan (text)
def diagnose(workflow: str) -> str:
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
        json={"model": "openai/gpt-oss-20b",
              "messages": [{"role": "user", "content": workflow}]},
    )
    return r.json()["choices"][0]["message"]["content"]

app = FastAPI()

class Workflow(BaseModel):                 # PACKAGE shape
    workflow: str

@app.post("/diagnose", status_code=201)    # ACTION + ADDRESS
def create_plan(body: Workflow, authorization: str = Header(None)):
    if authorization != "Bearer " + os.environ["SERVICE_KEY"]:   # KEY
        raise HTTPException(401)
    return {"plan": diagnose(body.workflow)}
