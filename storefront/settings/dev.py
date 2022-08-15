from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront4',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123abc',
        'PORT': 3307,
    }
}
