from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3StaticStorage',
    'S3DefaultStorage',
)

# for media
class S3DefaultStorage(S3Boto3Storage):
    default_acl = 'private'
    location = 'media'


class S3StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = 'static'


class S3ImageStorage(S3Boto3Storage):
    default_acl = 'private'
    location = 'media/image'


class S3FileStorage(S3Boto3Storage):
    default_acl = 'private'
    location = 'media/file'
