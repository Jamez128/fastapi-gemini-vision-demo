
"""
gemini_api.py

Helper module that wraps the Google Gemini API (multimodal model).
Provides a function 'vision' which takes a prompt and an image URL,
downloads the image, and sends both to Gemini for inference.
"""

import os # stdlib for environment variables
from google import genai # Google GenAI client (pip install google-genai)
from dotenv import load_dotenv # loads secrets from .env
import PIL.Image # Pillow image handling
import requests # HTTP requests

# Load environment variables from .env file into process
load_dotenv()

# Read API key from environment (make sure .env contains GOOGLE_API_KEY)
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

# Initialise the Gemini API client
client = genai.Client(api_key=GOOGLE_API_KEY)

def vision(prompt, img_url):
    """
    Run unference on the Gemini multimodal model with a text prompt + image.
    - Downloads the image from the given URL.
    - Opens it with Pillow (PIL).
    - Sends both the prompt and image to the Gemini model.
    - Returns the model's generated response text.
    
    Args:
        prompt (str): Instruction or question for the model.
        img_url (str): URL of an image (must be direct JPG/PNG, not a webpage).
        
    Returns:
        str: Model-generated text description/answer.
    """
    # Download image from the web (stream=True avoids loading all bytes into memory at once)
    img = PIL.Image.open(requests.get(img_url, stream=True).raw)

    # Call Gemini model for multimodal inference
    response = client.models.generate_content(
        model="gemini-1.5-flash", contents =[prompt, img]
    )

    return response.text