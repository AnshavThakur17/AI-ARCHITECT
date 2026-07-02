HEY EVERYONE,ANSHAV THIS SIDE.
TO RUN THIS PROJECT IN YOUR SYSTEM YOU SIMPLY NEED TO RUN THESE COMMMANDS

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

