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
            "Hello, I am Wrestlebot, ask me a question about wrestling."  # noqa: E501
        )
        self.SYSTEM_PROMPT = "You are a friendly yet laconic wrestling commentator. When asked a question, you respond with a short, witty answer with a link to more information."  # noqa: E501
        self.messages = [{"role": "system", "content": f"{self.SYSTEM_PROMPT}"}]
        self.chat_log = f"{self.FIRST_OUTPUT}\n"
        self.FILE = open("debug_log.txt", "w")

        # init openai interface
        openai.api_key = self.env["OPENAI_API_KEY"]
        # self.chat_completion = openai.ChatCompletion(engine="gpt-3.5-turbo")

    async def get_response(self, text: str) -> str:
        # get response from openai interface
        # prompt = f"{self.chat_log}\n{text}\n"
        self.messages.append({"role": "user", "content": f"{text}"})

        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0,
        )
        response = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": f"{response}"})
        return response
