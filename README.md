# guternberg_books
Guternberg books rest api with Python (Django)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/syedafrith/guternberg_books.git
$ cd guternberg
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Create new schema and import the data downloaded from https://drive.google.com/file/d/1Q3QZcy3fmltgLIwLsldPx_KYBOTNuAGA/view

Configuring your Mysqldb connection settings in django project
1) cd geternberg/geternberg/settings.py
2) open the settings file
   
Change the below values with your configurations
3) DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "", (Your scheme name created in above steps)
        "USER": "", # (Your mysql user name)
        "PASSWORD": "", # (Your password)
        "HOST": "127.0.0.1", (Your host)
        "PORT": "3306",
    }
}


Download and import the postman collection from (https://github.com/syedafrith/guternberg_books/blob/main/guternberg.postman_collection.json)

Run the Django server

```sh
(venv)$ python manage.py runserver
```

Finally test the api with the postman or any other api testing tool

If your running django server in local use the below api
http://localhost:8000/api/books/?page_no=1&book_id=1,24&language=en,fr&mimi_type=application/pdf&topic=child,infant&author=&title=adven
