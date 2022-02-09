# Traps
## 1. Migration
No need to add manage.py file, directly use `flask db init` for the 1st time. Then use `flask db migrate -m "message"` to generate migration scripts and `flask db upgrade` to migrate.
## 2. Flask version
Please use `pip install flask==1.1.4` instead of directly install which is Flask 2.x.x.
## 3. db=SQLAlchemy()
db is seperated to db.py file and used in this whole project. In this way the migration can only work fine.
## 4. Swagger
Use flasgger for Swagger UI, but don't use this for API doc generation. Please directly use Postman.
## 5. windows terminal migration issue
Related to PYTHONPATH. 
refer to https://blog.csdn.net/NeverLate_gogogo/article/details/107615838


# Tips
## 1. Folder structure
```
myapi/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure
    models.py       # contains models for ORM
    settings.py     # map secret configuration from .env
    .env            contains secret
```

