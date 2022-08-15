import os

from .dev import SECRET_KEY
from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["dan-prod.herokuapp.com"]

DATABASES = {
    'default': dj_database_url.config()
}
