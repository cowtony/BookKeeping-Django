# BookKeeping-Django
# TODO
- Deploy with HeroKu
- Deploy with AWS
- Login Authetication

# Developer's Manual
## Creating the project
- Create virtual environment: `python -m venv env`
- Install Django: `python -m pip install django`

Or install from requirments.txt file:
- Generate: `pip freeze > requirements.txt`
- Restore: `pip install -r requirements.txt`

- `django-admin startproject web_project .`
- `python manage.py startapp my_app`

## Update Database
- `python manage.py makemigrations`
- `python manage.py migrate`

## Other command
- `python manage.py runserver 8001`
- `python manage.py createsuperuser --username=<username> --email=<email>`

## Deploy
- `python manage.py collectstatic`
### [Deploy to HeroKu](https://devcenter.heroku.com/articles/django-app-configuration)

- `git push heroku master`


## Reference
[Django Document](https://docs.djangoproject.com/en/3.0/),
[Django + VScode Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)

