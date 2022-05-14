# BookKeeping-Django

# TODO
- HeroKu configure PostgreSQL
- Login Authetication
- Custom domains with HeroKu

# Developer's Manual

## [Django + VScode Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)

- Create a virtual environment: `python -m venv .venv` (a folder `.venv` will be created)
- Activate virtual environment: `source .venv/Scripts/activate`

Once in the virtual environment:
- Install Django: `python -m pip install django`
- Upgrade Django: `python -m pip install --upgrade Django`

Or install from `requirments.txt` file:
- Generate all required packages to file: `pip freeze > requirements.txt`
- Install from requirements: `pip install -r requirements.txt`

Create the first Django project:
- `django-admin startproject web_project .`

## manage.py

- `python manage.py startapp my_app`
- Update Database `python manage.py makemigrations`
- Update Database `python manage.py migrate`

## Other command
- `python manage.py runserver 8001`
- `python manage.py createsuperuser --username=<username> --email=<email>`

# HeroKu

## [Configuring Django Apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration)

- Create file `Procfile` at root with the following content:
  ```
  web: gunicorn myproject.wsgi
  ```
- Install gunicorn: `pip install gunicorn`

## [Deploying with Git](https://devcenter.heroku.com/articles/git)

- `python manage.py collectstatic`


- `pip install django-heroku`
- Procfile
- Add some lines in `settings.py`
- runtime.txt


- `git push heroku master`
- `heroku config`
Migrate database for heroku:
- `heroku run bash`
- `python manage.py migrate`
https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43

## Reference
[Django Document](https://docs.djangoproject.com/en/4.0/),
https://devcenter.heroku.com/articles/deploying-python