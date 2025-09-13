"""
api.py

FastAPI application that exposes a REST API around the Gemini vision helper.
Endpoints:
    GET /               -> Basic health check ("Hello World")
    POST /api/gemini    -> Run vision model with prompt + image URL
"""

from fastapi import FastAPI # main FastAPI framework
from gemini_api import vision # our helper function
import uvicorn # ASGI (asynchronous server gateway interface) server

# Create the FastAPI application object.
# This object holds all routes, configuration, and middleware.
app = FastAPI()

@app.get("/")
def read_root():
    """
    Health check endpoint.

    Returns:
        dict: Simple hellow-world response to confirm server is running.
    """
    return {"Hello": "World"}
 
@app.post("/api/gemini")
def gemini(prompt: str, img_url: str):
    """
    POST endpoint for Gemini Vision inference.

    Query Parameters:
        prompt (str): Instruction or question for the model.
        img_url (str): Direct image URL to analyse.

    Returns:
        dict: JSON object with Gemini model results.
    """
    return {"results": vision(prompt, img_url)}

if __name__ == "__main__":
    # When this file is executed directly (not imported), start the server.
    # Runs on localhost:8000 by default.
    uvicorn.run(app, port=8000)