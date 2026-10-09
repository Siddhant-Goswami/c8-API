# Deploy to Render as-is (start: python main.py). It runs; nothing can reach it.

import os, requests

# input: workflow (text)   output: plan (text)
def diagnose(workflow: str) -> str:
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
        json={"model": "openai/gpt-oss-20b",
              "messages": [{"role": "user", "content": workflow}]},
    )
    return r.json()["choices"][0]["message"]["content"]

print("diagnose() is on Render. How would anyone call it?")
