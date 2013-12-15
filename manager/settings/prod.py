"""
Django settings in production environment.
"""

# Imports
from __future__ import absolute_import
from .common import *
import os

# Administrators configuration
ADMINS = (
    ('Philippe Plagnol', 'philippe.plagnol@gmail.com'),
    ('Nicolas Pieuchot', 'nls.pct@gmail.com'),
)

# Managers configuration
MANAGERS = ADMINS

# Debug
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#debug

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = True

# Subsite configuration

SUBSITE = 'brand/'

# Allowed host
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#allowed-ho
# sts

ALLOWED_HOSTS = [
    'brand-okfn.herokuapp.com', 'product.okfn.org', 'brand.product.okfn.org']

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
CACHEFILES_STORAGE = 'manager.libs.snippets.s3.CacheRootS3BotoStorage'
COMPRESS_STORAGE = 'manager.libs.snippets.s3.CacheRootS3BotoStorage'

AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = "s3-eu-west-1.amazonaws.com/"
AWS_S3_URL_PROTOCOL = 'https'
AWS_S3_SECURE_URLS = True
AWS_IS_GZIPPED = True

S3_URL = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

STATIC_DIRECTORY = 'brand/static'
AWS_STATIC_URL = "%s/%s" % (S3_URL, STATIC_DIRECTORY)
STATIC_URL = "%s://%s/" % (AWS_S3_URL_PROTOCOL, AWS_STATIC_URL)

MEDIA_DIRECTORY = 'brand/media'
AWS_MEDIA_URL = "%s/%s" % (S3_URL, MEDIA_DIRECTORY)
MEDIA_URL = "%s://%s/" % (AWS_S3_URL_PROTOCOL, AWS_MEDIA_URL)

CACHE_DIRECTORY = 'brand/cache'
AWS_CACHE_URL = "%s/%s" % (S3_URL, CACHE_DIRECTORY)

# Compress configuration
# http://django-compressor.readthedocs.org/en/master/remote-storages/using-sta
# ticfiles

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

# Email configuration for sendgrid
# http://sendgrid.com/docs/Integrate/Frameworks/django.html

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

# Allow some friendly domains
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-domain

SESSION_COOKIE_DOMAIN = 'product.okfn.org'
CSRF_COOKIE_DOMAIN = 'product.okfn.org'

RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_USE_SSL = True
