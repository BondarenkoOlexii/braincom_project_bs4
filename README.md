# Installation

Create and activate a virtual environment:

python -m venv venv

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Install Playwright browsers:

playwright install Environment variables

Create a .env file in the project root:

# DJANGO

SECRET_KEY=django-insecure-mbvh03e+9rmomqmnf9=l)09byu-sa+2-@pfoty)rnrbj#d0fu8

DEBUG=TRUE

ALLOWED_HOSTS=localhost,127.0.0.1

# POSTGRES

DB_ENGINE=django.db.backends.postgresql

DB_NAME=braincom_project_playwright

DB_USER=postgres

DB_PASSWORD=1

DB_HOST=localhost

DB_PORT=5432

#

Make sure PostgreSQL is running and the database exists.

Database setup

Run migrations:

cd braincom_project python manage.py migrate

Return to the project root:

cd .. Running the parser

Run:

python modules/parse_data.py
