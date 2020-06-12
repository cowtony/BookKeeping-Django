# BookKeeping-Django
# TODO
- HeroKu configure PostgreSQL
- Deploy with AWS
- Login Authetication
- Custom domains with HeroKu

# Developer's Manual
## Creating the project
- Create virtual environment: `python -m venv env`
- Activate virtual environment: `source env/Scripts/activate`
- Install Django: `python -m pip install django`
- Upgrade Django: `python -m pip install --upgrade Django`

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
https://devcenter.heroku.com/articles/deploying-python
https://devcenter.heroku.com/articles/django-app-configuration
https://devcenter.heroku.com/articles/git
- `pip install gunicorn`
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
[Django Document](https://docs.djangoproject.com/en/3.0/),
[Django + VScode Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)

