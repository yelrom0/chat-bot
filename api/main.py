"""The main file of the application. This is where hypercorn comes to play."""

# System Imports

# Package Imports
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values

# Local Imports
# from api.load_html import html_file
from api.open_ai_api import AIApi

# create main server
app = FastAPI(
    title="Chatbot",
    description="A simple chatbot that uses OpenAI to respond to user input. Now with ChatGPT.",  # noqa: E501
    version="1.0.0",
)

# import the html as a template
templates = Jinja2Templates(directory="site")


@app.get("/", response_class=HTMLResponse)
async def get_frontend(request: Request):
    # load the values from the environment variables
    env = dotenv_values(".env")

    # load the html file using jinja2 and return it
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "hostname": env["WEBSOCKET_BACKEND"],
        },
    )


@app.websocket("/")
async def chatbot_connection(websocket: WebSocket):
    await websocket.accept()
    # setup api and send first message back to client
    ai_api = AIApi()
    init_msg = await websocket.receive_text()

    if not init_msg:
        await websocket.send_text(ai_api.FIRST_OUTPUT)
    else:
        ai_api.chat_log = f"{init_msg}\n"

    while True:
        message = await websocket.receive_text()

        if message != '{ "id": 0 }':
            response = ai_api.get_response(message)
        else:
            response = ""

        await websocket.send_text(response)
