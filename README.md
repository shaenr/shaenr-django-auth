# shaenr-django-auth
+ Based on django-allauth
+ The current Facebook login feature is not currently approved by Facebook.
+ https over localhost is working for the test app
+ The templates are not pretty but everything works.

> REMEMBER: CHANGE THE `SECRET_KEY` AND `DEBUG = False` IN SETTINGS FILE BEFORE USING THIS IN PRODUCTION!

---

### Custom User Model
+ Removed fields: *username*, uses email for auth field

### Docker Postgres Database
Use docker to run postgres db using the config in `settings.py`

```bash
docker pull postgres
docker run 
    --name pg 
    -v /tmp/my-pgdata:/var/lib/postgresql/data 
    -e POSTGRES_PASSWORD=password 
    -p 127.0.0.1:5432:5432 
    -d postgres
```

From another shell...

```bash
docker exec -it pg su postgres
psql -c "GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;"
```

### Django Setup

You'll need testing `django_project/.env` file:

```dotenv
NAME=postgres
USER=postgres
PASSWORD=password
HOST=127.0.0.1
PORT=5432
```

Then you can do:

```bash
python -m pip install -r requirements.txt
# Setup Postgres Database (see above)
python manage.py makemigrations
python manage.py migrate
python manage.py
python manage.py createsuperuser --email admin@admin.com

python manage.py runsslserver     # NOTE this is a different command that usual!
```

---

### TODO

+ I should write some test cases and go from there...
+ I should implement a basic frontend layout...
+ I should write a logger.
