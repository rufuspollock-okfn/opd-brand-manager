# -*- coding: utf-8 -*-
# Copyright (C) 2012 ZERO GACHIS SAS - All Rights Reserved

""" Amazon Web Services S3 utils
"""

# Django imports
from django.conf import settings

# Other imports
from storages.backends.s3boto import S3BotoStorage


class StaticRootS3BotoStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = settings.S3_URL
        kwargs['location'] = settings.STATIC_DIRECTORY
        super(StaticRootS3BotoStorage, self).__init__(*args, **kwargs)


class MediaRootS3BotoStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = settings.S3_URL
        kwargs['location'] = settings.MEDIA_DIRECTORY
        super(MediaRootS3BotoStorage, self).__init__(*args, **kwargs)
