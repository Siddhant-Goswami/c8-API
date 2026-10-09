# V3: chat calls your Render API. HF Space secrets: RENDER_URL, SERVICE_KEY

import os, requests, gradio as gr
from dotenv import load_dotenv

load_dotenv()

def respond(message, history):
    r = requests.post(os.environ["RENDER_URL"] + "/diagnose",
                      headers={"Authorization": "Bearer " + os.environ["SERVICE_KEY"]},
                      json={"workflow": message},
                      timeout=90)   # free Render sleeps; first call takes 30-60s
    return r.json()["plan"]

gr.ChatInterface(fn=respond).launch()
