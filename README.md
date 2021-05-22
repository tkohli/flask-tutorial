# flask-tutorial
 A new flask project following the tutorial on https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/

 The project directory will contain:

flaskr/, a Python package containing your application code and files.

tests/, a directory containing test modules.

venv/, a Python virtual environment where Flask and other dependencies are installed.

Installation files telling Python how to install your project.

Version control config, such as git. You should make a habit of using some type of version control for all your projects, no matter the size.

Any other project files you might add in the future.

By the end, your project layout will look like this:

/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in


Application Setup
A Flask application is an instance of the Flask class. Everything about the application, such as configuration and URLs, will be registered with this class.

The most straightforward way to create a Flask application is to create a global Flask instance directly at the top of your code, like how the “Hello, World!” example did on the previous page. While this is simple and useful in some cases, it can cause some tricky issues as the project grows.

Instead of creating a Flask instance globally, you will create it inside a function. This function is known as the application factory. Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.

##The Application Factory
It’s time to start coding! Create the flaskr directory and add the __init__.py file. The __init__.py serves double duty: it will contain the application factory, and it tells Python that the flaskr directory should be treated as a package.
