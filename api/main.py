"""The main file of the application. This is where hypercorn comes to play."""

# System Imports

# Package Imports
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

# Local Imports
from api.load_html import html_file

app = FastAPI(
    title="Chatbot",
    description="A simple chatbot that uses OpenAI to respond to user input.",
    version="0.0.1",
)


@app.get("/", response_class=HTMLResponse)
def get_frontend():
    return html_file()


@app.websocket("/")
async def chatbot_connection(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        print(f"server received: {message}")
        await websocket.send_text(f"message was: {message}")
