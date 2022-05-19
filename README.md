# BookKeeping-Django

# TODO
- HeroKu configure PostgreSQL
- Login Authetication
- Custom domains with HeroKu

# Developer's Manual

Ref: [Django + VScode Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)

## Initial environment setup
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

- `python manage.py startapp <my_app>`
  Creates a folder called <my_app> that contains a number of code files and one subfolder.
- `python manage.py collectstatic`
  For **production** deployments, you typically collect all the static files from your apps into a single folder.

Database changes:
1. Make changes to the models in your `models.py` file.
1. `python manage.py makemigrations`
   Generate scripts in the `migrations` folder that migrate the database from its current state to the new state.
1. `python manage.py migrate`
   Apply the scripts to the actual database.

## Testing
- Staart local server: `python manage.py runserver 8001`
- `python manage.py createsuperuser --username=<username> --email=<email>`

# Deploy to HeroKu

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

Push the changes to GitHub then:
- `git push heroku master`
- `heroku config`
Migrate database for heroku:
- `heroku run bash`
- `python manage.py migrate`
https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43

## Reference
[Django Document](https://docs.djangoproject.com/en/4.0/),
https://devcenter.heroku.com/articles/deploying-python