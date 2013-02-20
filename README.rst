django-request-log
==================

django-request-log is pluggable Django application to keep track user login and logout events and URLs views 
developed at ORCAS.

Quickstart
==========

Installation
------------

django-request-log is available on PyPI, so you can install it with ``pip``::

    $ pip install django-request-log

Or add the line below to the project's requirement file::

    django-request-log

Usage
-----

1. Add ``log`` to your ``INSTALLED_APPS``.

2. Add ``log.middleware.RequestLoggingMiddleware`` to your ``MIDDLEWARE_CLASSES``::

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        ...
        'log.middleware.RequestLoggingMiddleware',
    )

3. Run::

    $ python manage.py syncdb

TODOs and BUGS
==============

See: https://github.com/orcasgit/django-request-log/issues
