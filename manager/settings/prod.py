"""
Django settings in production environment.
"""

# Imports
from __future__ import absolute_import
from .common import *

# Debug
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#debug

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = True

# Allowed host
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#allowed-ho
# sts

ALLOWED_HOSTS = ['brand-okfn.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Secret key
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#secret-key
# Set with heroku config:add DJANGO_SECRET_KEY="<random string>"

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Parse database configuration from $DATABASE_URL
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#databases

import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# https://docs.djangoproject.com/en/1.6/ref/settings/#secure-proxy-ssl-header

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#static-root
# -and-static-url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
