# FastAPI + Google Gemini Vision Demo
A simple FastAPI application that wraps the Google Gemini multimodal model.
You provide a **text prompt** and an **image URL**, and the API returns the Gemini's generated description/answer.

This project demonstrates:
* Using **FastAPI** to build a web API
* Running an **ASGI Server (Uvicorn)**
* Handling environment variables with dotenv
* Making requests to **Google's Gemini API**
* Processing images with **Pillow (PIL)**
* Documenting an API with **Swagger UI** (built into FastAPI)

Getting Started```
1. Clone the repository
git clone https://github.com/yourusername/my-fastapi-gemini-app.git
cd my-fastapi-gemini-app```

2. Create a virtual environment```
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows PowerShell```

3. Install dependencies```
pip install -r requirements.txt```

4. Set up environment variables```
Copy .env.example into a real .env file:
cp .env.example .env

Edit .env and add your Google API key:
GOOGLE_API_KEY=your_api_key_here```

5. Run the server```
uvicorn api:app --reload

The API will be available at:
* http://127.0.0.1:8000 -> root health check
* http://127.0.0.1:8000/docs -> Swagger UI (interactive docs)
* http://127.0.0.1:8000/redoc -> ReDoc API docs```

API Endpoints```
GET /
Health check endpoint.
{
    "Hello": "World"
}

POST /api/gemini
Run Gemini Vision inference on an image```

**Query Parameters**
* prompt (str): Instruction/question to ask the model
* img_url (str): Direct link to an image (JPG/PNG)

**Example Request**
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/gemini?prompt=What%20is%20this%20a%20picture%20of%3F&img_url=https%3A%2F%2Fa.travel-assets.com%2Ffindyours-php%2Fviewfinder%2Fimages%2Fres70%2F542000%2F542607-singapore.jpg'
```

**Example Response**
```
{
  "results": "That's a picture of Marina Bay Sands in Singapore at night.  The image shows the iconic hotel towers with their rooftop infinity pool, along with the ArtScience Museum and other buildings in the Marina Bay Sands complex.  The calm water provides a perfect reflection of the illuminated structures.\n"
}
```

**Project Structure**
```
.
├── api.py             # FastAPI app & endpoints
├── gemini_api.py      # Gemini client wrapper (vision helper)
├── requirements.txt   # Project dependencies
├── .env.example       # Example environment variables
├── .gitignore         # Ignore venv, .env, etc.
└── README.md          # Project documentation
```