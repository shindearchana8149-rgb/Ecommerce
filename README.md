Minimal Django e-commerce starter.
Commands:
python -m venv .venv
# activate it
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Create admin user:
python manage.py createsuperuser
