# V1: echo chat (last lecture). Run: python 01_echo_chat.py

import gradio as gr

def respond(message, history):
    return "You typed: " + message

gr.ChatInterface(fn=respond).launch()
