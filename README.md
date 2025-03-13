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

## Deploying to Render.com

1. Push your changes to GitHub:
   ```
   git add .
   git commit -m "Prepared for Render deployment"
   git push origin main
   ```

2. Log in to Render.com and create a new Web Service.

3. Connect to your GitHub repository.

4. Configure the following settings:
   - **Name**: SkillEdge (or any name you prefer)
   - **Environment**: Python
   - **Region**: Choose the one closest to your users
   - **Branch**: main
   - **Build Command**: `./build.sh`
   - **Start Command**: `cd SkillEdge-root && gunicorn SkillEdge.wsgi:application`
   - **Plan**: Free

5. Add the following environment variables in the Render dashboard:
   - `GEMINI_API_KEY`: Your Gemini API key
   - `SECRET_KEY`: A secure random string (Django secret key)
   - `DEBUG`: false
   - `PYTHON_VERSION`: 3.10 (or your preferred version)

6. Click "Create Web Service" and Render will automatically deploy your application.

7. (Optional) Create a PostgreSQL database on Render:
   - Go to the Render dashboard and create a new PostgreSQL database
   - Render will automatically create a `DATABASE_URL` environment variable
   - Link the database to your web service

8. Your application will be available at the URL provided by Render. 