orcas-log
=========

orcas-log is pluggable Django application to keep track user login and logout events and URLs views 
developed at ORCAS.

Installation
============

1. Add ``log`` to your ``INSTALLED_APPS``.

2. Add ``log.middleware.RequestLoggingMiddleware`` to your ``MIDDLEWARE_CLASSES``
````
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        ...
        'log.middleware.RequestLoggingMiddleware',
    )
````

3. Add the line below to the project's  ``requirement.txt`` file:
````
   git+https://github.com/orcasgit/django-request-log.git#egg=request-log
````

4. Run:
````
    pip install -U -r requirements.txt
````

TODOs and BUGS
==============

1. Add tests
2. Update LICENCE
