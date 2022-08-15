import os

from .dev import SECRET_KEY
from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["dan-prod.herokuapp.com"]

# DATABASE_URL = 'postgres://aqqdqfgrxknrxm:943a7e5c8bdaf82da35557bca2575b09eee8f4d351d1c5518db01632ca1a1c0c@ec2-107-22-238-112.compute-1.amazonaws.com:5432/dfmanspfpl6ufv'
DATABASES = {
    'default': dj_database_url.config(env='HEROKU_POSTGRESQL_MAROON_URL')
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        'TIMEOUT': 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
