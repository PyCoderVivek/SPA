# SkillEdge - SPA (Single Page Application)

A comprehensive Django web application for skill development, career roadmaps, and community learning.

## Deployment to Render.com

This project is configured for easy deployment to Render.com.

### Prerequisites

- A Render.com account (free tier works)
- A GitHub repository with your code (already set up at https://github.com/PyCoderVivek/SPA.git)

## Local Development

1. Clone the repository:
   ```
   git clone https://github.com/PyCoderVivek/SPA.git
   cd SPA
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env` file:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

5. Run migrations and start the server:
   ```
   cd SkillEdge-root
   python manage.py migrate
   python manage.py runserver
   ```

## AVAILABLE AT 

https://spa-em9r.onrender.com
