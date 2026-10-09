# Backend stripped: input -> process -> output, no Gradio. Run: python 05_diagnose.py

import os, requests
from dotenv import load_dotenv

load_dotenv()

# input: workflow (text)   output: plan (text)
def diagnose(workflow: str) -> str:
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
        json={"model": "openai/gpt-oss-20b",
              "messages": [{"role": "user", "content": workflow}]},
    )
    return r.json()["choices"][0]["message"]["content"]

# quick check
print(diagnose("Every Monday I open Jira, pick high-priority to-dos, "
               "pull dashboard numbers, write a report, and send it on Slack."))
