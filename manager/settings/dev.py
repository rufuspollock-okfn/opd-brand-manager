"""
Django settings in development environment.
"""

# Imports
from __future__ import absolute_import
from .common import *

# Debug
# https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-DEBUG

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = False

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pod_brand',
        'USER': 'pod',
        'PASSWORD': 'pod',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
