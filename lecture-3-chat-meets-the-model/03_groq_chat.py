# V2: chat calls Groq. Run: python 03_groq_chat.py

import os, requests, gradio as gr
from dotenv import load_dotenv

load_dotenv()   # key comes from .env, never typed in the file

def respond(message, history):
    r = requests.post(                                   # ACTION
        "https://api.groq.com/openai/v1/chat/completions",  # ADDRESS
        headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},  # KEY
        json={"model": "openai/gpt-oss-20b",              # PACKAGE
              "messages": [{"role": "user", "content": message}]},
    )
    return r.json()["choices"][0]["message"]["content"]

gr.ChatInterface(fn=respond).launch()
