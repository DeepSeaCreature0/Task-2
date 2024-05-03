#!/bin/bash

# Apply database migrations
python manage.py makemigrations

python manage.py migrate

# Populate the database
python manage.py populate

# Start Django server
python manage.py runserver 0.0.0.0:8000
