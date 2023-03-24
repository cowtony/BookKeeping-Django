# TODO
- Login feature
- **Deploy** to PythonAnywhere or HeroKu
  - HeroKu configure PostgreSQL
  - Custom domains with HeroKu
- Use .env file to protect sensitive info such as DB password:

```.env
SECRET_KEY=8k3f^1e+5kwf1tuf@-xvq$f=i7%w+%a0giz#u7er#5uf)q0rr2
DB_NAME=book_keeping
DB_USER=cowtony
DB_PASSWORD=19900525
DB_HOST=localhost
DB_PORT=5432
```

```python
import environ
env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
```