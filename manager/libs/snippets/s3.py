# -*- coding: utf-8 -*-
# Copyright (C) 2012 ZERO GACHIS SAS - All Rights Reserved

""" Amazon Web Services S3 utils
"""

# Django imports
from django.conf import settings

# Other imports
from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='brand/static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='brand/media')
