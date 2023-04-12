"""
open_ai_api.py
The backend functions of this application.
Most of this code is taken from my previously written terminal.py file.
"""

# System Imports

# Package Imports
import openai
from dotenv import dotenv_values


class AIApi:
    def __init__(self):
        # Load environment variables
        self.env = dotenv_values(".env")

        # Constants
        self.FIRST_OUTPUT = (
            "Hello, I am Sportsbot, ask me a question about sports."  # noqa: E501
        )
        self.SYSTEM_PROMPT = "You are a friendly yet laconic sports commentator. When asked a question, you respond with a short, witty answer with a link to more information."  # noqa: E501
        self.messages = [{"role": "system", "content": self.SYSTEM_PROMPT}]
        self.chat_log = f"{self.FIRST_OUTPUT}\n"
        self.FILE = open("debug_log.txt", "w")

        # init openai interface
        openai.api_key = self.env["OPENAI_API_KEY"]
        self.chat_completion = openai.ChatCompletion()

    def get_response(self, text: str) -> str:
        # get response from openai interface
        # prompt = f"{self.chat_log}\n{text}\n"
        messages = self.messages.append({"role": "user", "content": text})
        response = ""
        # loop to stop blank responses
        while not response:
            response = self.chat_completion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0,
            )
            response = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "system", "content": response})
        return response
