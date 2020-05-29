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
- `echo 'web: gunicorn web_project.wsgi' > Procfile`
- append the following code to `settings.py`:
```
import django_heroku
django_heroku.settings(locals()) 
```
- `git push heroku master`
https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43

## Reference
[Django Document](https://docs.djangoproject.com/en/3.0/),
[Django + VScode Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)

