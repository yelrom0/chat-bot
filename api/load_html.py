"""
load_html.py
Code to load the HTML file for the web app, to be returned by the API.
"""

# System Imports
import codecs

# Package Imports
from fastapi.responses import HTMLResponse

# Local Imports


"""
Load the HTML file for the web app, to be returned by the API.
"""


def html_file() -> HTMLResponse:
    with codecs.open("./site/index.html", "r", "utf-8") as file:
        return file.read()
