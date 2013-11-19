# -*- coding: utf-8 -*-
# Copyright (C) 2012 ZERO GACHIS SAS - All Rights Reserved

""" Amazon Web Services S3 utils
"""

# Django imports
from django.conf import settings
from django.core.files.storage import get_storage_class

# Other imports
from storages.backends.s3boto import S3BotoStorage


class CachedS3BotoStorage(S3BotoStorage):
    """
    django-compressor uses this class to gzip the compressed files and
    send them to s3 these files are then saved locally, which ensures that
    they only create fresh copies when they need to
    """

    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            'compressor.storage.GzipCompressorFileStorage')()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name


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


class CacheRootS3BotoStorage(CachedS3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = settings.S3_URL
        kwargs['location'] = settings.CACHE_DIRECTORY
        super(CacheRootS3BotoStorage, self).__init__(*args, **kwargs)
