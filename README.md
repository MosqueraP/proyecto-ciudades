## Instalación:

```
python -m venv venv

# Activación en Unix
source venv/bin/activate

# Activación en Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Para crear un super usuario y acceder al admin:

```
python manage.py createsuperuser
```
