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

# Django storage installation requirements
# http://django-storages.readthedocs.org/en/latest/#installation

INSTALLED_APPS += (
    'storages',
)

# Static asset configuration for S3
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#static-root
# -and-static-url

AWS_STORAGE_BUCKET_NAME = 'product.okfn.org'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
STATICFILES_STORAGE = 'manager.libs.snippets.s3.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE = 'manager.libs.snippets.s3.MediaRootS3BotoStorage'

AWS_QUERYSTRING_AUTH = True
AWS_S3_URL_PROTOCOL = 'https'
AWS_S3_SECURE_URLS = True
AWS_IS_GZIPPED = True

S3_URL = '%s://s3.amazonaws.com/%s/' % (
    AWS_S3_URL_PROTOCOL,
    AWS_STORAGE_BUCKET_NAME
)

STATIC_DIRECTORY = 'brand/static/'
STATIC_URL = S3_URL + STATIC_DIRECTORY

MEDIA_DIRECTORY = 'brand/media/'
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
