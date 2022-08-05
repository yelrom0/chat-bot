# Chat Bot

Self explanatory, a bot, you chat to it.

## How Do I use it?

_note: This guide is for Linux/Mac and assumes you have docker and docker-compose installed. If you're running Windows, use WSL._

1. If you haven't already, get an OpenAI API key at [Open AI](https://beta.openai.com/).
2. Next, copy `default.env` to `.env`, as `.env` is what's actually read by the backend.
3. Set your API key, TTS_ENABLED (if running on command line on MacOS), and WEBSOCKET_BACKEND (if running the web version) in `.env`. The comments in `.env` explain each of these.
4. Run `docker-compose up -d` to build the image and start the backend.
5. Open your browser and go to `http://localhost:8000`. If this doesn't work, check that no services are already running on port 8000.
6. Talk to the chatbot.
7. Enjoy!

## Why did I make it?

- I was talking to a friend who wasn't sure where to start for a project to learn Python, and mentioned that he wanted to make a chatbot. So on a call with him, I just started coding this. It started as a basic showing of functions and conditionals, but within a few hours I had a working chatbot. So really, it's just a lesson on something small can turn into a larger project, piece-by-piece.

## What Stack Does It Use?

- For the web framework it uses FASTAPI, a fast, lightweight web framework for Python. Then forwards a html template to the browser using jinja2 templates. The frontend is built using vanilla javascript and connects to the backend via websockets. On the backed I connect to the OpenAI API and use the completion library configured in a specific way to respond to the user.

## Can I modify it?

- Sure! Feel free to modify it and share it with the world.

## Can I test it without running it myself?

- _sigh_ yes, as long as you don't break anything [ChatBot @ Morley's Exact Club](https://chatbot.morleysexact.club)

## Will you update this in the future?

- Likely every so often, if issues come up possibly, but less likely to do so as it was meant as just a small learning project. ¯\\\_(ツ)\_/¯

## Who am I?

- I'm Daniel Morley, a Backend Python Developer from Melbourne, Australia. I enjoy tinkering with my home server and sometimes write small projects like this (and sometimes some larger).
