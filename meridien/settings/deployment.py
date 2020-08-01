import os

import django_heroku
import dj_database_url

from meridien.settings.base import *

# Static files

STATIC_ROOT = 'static'

# Security

DEBUG = False

SECRET_KEY = os.getenv('MERIDIEN_SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = dict()
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# CORS settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    os.getenv('MERIDIEN_FRONT_END_DOMAIN'),
)

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('MERIDIEN_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('MERIDIEN_EMAIL_PASSWORD')

# Communication settings

ALLOWED_HOSTS += [
    os.getenv('MERIDIEN_DOMAIN')
]

CSRF_COOKIE_SECURE = True

FRONT_END_DOMAIN = os.getenv('MERIDIEN_FRONT_END_DOMAIN')

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

# Activate Django-Heroku.
django_heroku.settings(locals())
