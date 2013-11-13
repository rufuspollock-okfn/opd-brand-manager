"""
Django settings in development environment.
"""

# Imports
from __future__ import absolute_import
from .common import *

# Debug configuration
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = False

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pod_brand',
        'USER': 'pod',
        'PASSWORD': '$2a$12$FDdOzdKSDtmIorJXhjvNDO',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
