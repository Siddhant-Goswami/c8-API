# Lecture 3: Chat Meets the Model

One function, three bodies: echo → Groq → your own API.

| File | Step |
|---|---|
| `01_echo_chat.py` | V1: echo chat |
| `02_call_groq.py` | Call Groq from Python |
| `03_groq_chat.py` | V2: chat calls Groq |
| `04_swap_api.py` | Homework: swap in any public API |
| `05_diagnose.py` | Backend stripped to input → output |
| `06_bare_on_render/` | Bare function on Render (unreachable) |
| `07_fastapi/` | FastAPI `POST /diagnose` on Render |
| `08_two_machines/` | V3: HF Space chat → Render API |

Setup: `pip install gradio requests python-dotenv fastapi uvicorn`, then `cp .env.example .env` and add your keys.
