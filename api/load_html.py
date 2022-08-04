"""
load_html.py
Code to load the HTML file for the web app, to be returned by the API.
"""

# System Imports
import codecs

# Package Imports

# Local Imports


"""
Load the HTML file for the web app, to be returned by the API.
"""
with codecs.open("./site/index.html", "r", "utf-8") as file:
    html_file = file.read()
