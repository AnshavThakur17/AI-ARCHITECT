HEY EVERYONE, ANSHAV THIS SIDE.

🔗 LIVE DEMO: https://ai-architect-d2vd.onrender.com/

PROJECT STRUCTURE
This project has BOTH frontend and backend in this single repo — nothing is split into a separate repository.

- The backend is built with FastAPI (Python).
- The frontend (HTML/CSS/JS) is located at: backend/app/templates/index.html
- The backend serves the frontend directly, so there is no separate "frontend" folder — it's all part of the same backend/app structure.

TO RUN THIS PROJECT IN YOUR SYSTEM YOU SIMPLY NEED TO RUN THESE COMMANDS

AI Architect Setup

Clone the repository:

git clone YOUR_REPO_URL

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a `.env` file in the backend folder.

Copy values from `.env.example` and add your own API keys.

Run backend:

uvicorn app.main:app --reload

Once the server is running, open your browser and go to:
http://127.0.0.1:8000

This will load the frontend (index.html) directly — since the backend serves it, you don't need to run anything separately for the frontend.
