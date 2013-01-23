orcas-log
=========

orcas-log is pluggable Django application to keep track user login and logout events and URLs views 
developed at ORCAS.

Installation
============

1. Add ``log`` to your ``INSTALLED_APPS``.

2. Add ``log.middleware.RequestLoggingMiddleware`` to your ``MIDDLEWARE_CLASSES``

3. Add the line below to the project's  ``requirement.txt`` file
````
   git+https://github.com/orcasgit/orcas-log.git#egg=orcas-log
````

4. Run
````
    pip install -U -r requirements.txt
````

TODOs and BUGS
==============
