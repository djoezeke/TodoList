#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Building the project..."

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Run Django migrations
echo "Running Django migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build process completed successfully."