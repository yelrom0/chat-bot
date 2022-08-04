"""The main file of the application. This is where hypercorn comes to play."""

# System Imports

# Package Imports
from fastapi import FastAPI

# Local Imports

app = FastAPI(
    title="Chatbot",
    description="A simple chatbot that uses OpenAI to respond to user input.",
    version="0.0.1",
)


@app.get("/")
def hello_world():
    return {"Hello": "World"}
