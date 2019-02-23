python3 -m pip install -U pip setuptools wheel
python3 -m install -U django

python3 manage.py makemigrations
python3 manage.py makemigrations jobs
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser