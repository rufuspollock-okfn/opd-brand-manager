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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

if SUBSITE:
    STATIC_URL = '/%s' % os.path.join(SUBSITE, *(STATIC_URL.split('/')))

# Compress configuration
# http://django-compressor.readthedocs.org/en/master/remote-storages/using-sta
# ticfiles

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OUTPUT_DIR = '/cache/'
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'

MEDIA_ROOT = 'media/'
MEDIA_URL = 'https://s3.amazonaws.com/product.okfn.org/brand/media/'

RECAPTCHA_PUBLIC_KEY = '6LcA1-sSAAAAAOa3yA3qXPheVoWonfC7Q_FonUHv'
RECAPTCHA_PRIVATE_KEY = '6LcA1-sSAAAAAGOcGs06xneAXU87b0U0pRTaSzig'
RECAPTCHA_USE_SSL = True

# Site ID
# https://docs.djangoproject.com/en/1.6/ref/contrib/sites/#enabling-the-sites-
# framework

SITE_ID = 2
