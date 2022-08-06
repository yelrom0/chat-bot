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
        self.FIRST_OUTPUT = "Hello, I am a chat bot. Ask me anything."
        self.chat_log = f"{self.FIRST_OUTPUT}\n"
        self.FILE = open("debug_log.txt", "w")

        # init openai interface
        openai.api_key = self.env["OPENAI_API_KEY"]
        self.completion = openai.Completion()

    def get_response(self, text: str) -> str:
        # get response from openai interface
        prompt = f"{self.chat_log}\n{text}\n"
        response = ""

        # loop to stop blank responses
        while not response:
            response = self.completion.create(
                prompt=prompt,
                engine="text-davinci-002",
                stop="\n\n",
                temperature=1,
                top_p=1,
                frequency_penalty=1,
                presence_penalty=-0.6,
                best_of=1,
                max_tokens=512,
            )
            response = response.choices[0].text.strip()

        return response
