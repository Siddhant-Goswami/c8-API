# Call Groq from plain Python. Run: python 02_call_groq.py

import os, requests
from dotenv import load_dotenv

load_dotenv()   # reads GROQ_API_KEY from .env

workflow = ("Every Monday I open Jira to check my weekly to-dos. "
            "I pick the high-priority ones, pull the numbers from our dashboard, "
            "write a short report for each, and send it to my manager on Slack.")

r = requests.post(                                                      # ACTION
    "https://api.groq.com/openai/v1/chat/completions",                  # ADDRESS
    headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},  # KEY
    json={"model": "openai/gpt-oss-20b",                                # PACKAGE
          "messages": [{"role": "user", "content": workflow}]},
)

print("Status code:", r.status_code)                                    # predict it first
print(r.json()["choices"][0]["message"]["content"])
