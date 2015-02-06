"""
Use for testing on sqlite3...

$ ./manage.py test
"""
import os

from django import VERSION

PROJECT_NAME = 'request-log'
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test.db',
        'USER': PROJECT_NAME,
        'PASSWORD': PROJECT_NAME,
        'HOST': '',
    }
}
django_14 = VERSION[0:2] == (1,4)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'log'
) + (('django_nose',) if django_14 else tuple())
if django_14:
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'log.middleware.RequestLoggingMiddleware',
)

USE_TZ = True
ROOT_URLCONF = 'testproject.urls'
SECRET_KEY = '&6hr-f+2+5k!$-oq6*l7p79+^+txtckz7imdoi%!a&0h1t3d(@'
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)
