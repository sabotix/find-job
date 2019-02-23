ECHO OFF

python -m pip install -U pip setuptools wheel
python -m install -U django
python manage.py makemigrations
python manage.py makemigrations jobs
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
PAUSE