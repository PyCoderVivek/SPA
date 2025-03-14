#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
cd SkillEdge-root
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate 