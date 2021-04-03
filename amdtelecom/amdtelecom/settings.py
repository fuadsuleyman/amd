"""
Django settings for amdtelecom project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#p_$i#w56)lc@6a0)nz6&#%)3d8+yy62+-xy9zxa#6on-e!a5&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get('DEBUG') else True
PROD = not DEBUG


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',

    'contact.apps.ContactConfig',
    'product.apps.ProductConfig',
    'account.apps.AccountConfig',
    'order.apps.OrderConfig',
    'index.apps.IndexConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'corsheaders',
    #'debug_toolbar',
    'colorfield',
    'rest_framework',
    # 'django_celery_beat',

]

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 1
# }




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'amdtelecom.urls'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost"
]

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'amdtelecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if PROD:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'amd_db_new',
            'USER' : 'amd_user',
            'PASSWORD' : 'password4474',
            'HOST' : '127.0.0.1',
            'PORT' : '5432',
        }
    }

if PROD:
    CELERY_BROKER_URL = 'redis://redis:6379'
    CELERY_RESULT_BACKEND = 'redis://redis:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Baku'
else:
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Baku'



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# REST_FRAMEWORK = {
#     # 'DEFAULT_PERMISSION_CLASSES':["rest_framework.permissions.IsAuthenticated"],
#     'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
#     'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
# }

# REST_FRAMEWORK = {
#     # 'DEFAULT_PAGINATION_CLASS': 'product.api.pagination.CustomProductPaginator',
#     'PAGE_SIZE': 3
# }

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    'localhost',
    # ...
]

# PHONE NUMBER CONFIG
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'az'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SITE_ADDRESS = 'http://localhost:8000'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

if PROD:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

if PROD:
    API_URL = 'http://143.110.156.62/'
else:
    # url = os.environ.get('POSTGRES_DB')
    # url =url.split(',')
    # print(url, 'datalar')
    API_URL = 'http://localhost:8000/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

SITE_URL = 'http://localhost:80'

# Image django resized
# DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
# DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
# DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
# DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True




JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]


# Email Settings
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'husubayli@gmail.com'
EMAIL_HOST_PASSWORD = 'xdjnasiuddxikfax'

# if settings.PROD:
#     app.conf.update(
#         BROKER_URL='redis://:{password}@redis:6379/0'.format(password=os.environ.get("REDIS_PASSWORD")),
#         CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
#         CELERY_RESULT_BACKEND='redis://:{password}@redis:6379/1'.format(password=os.environ.get("REDIS_PASSWORD")),
#         CELERY_DISABLE_RATE_LIMITS=True,
#         CELERY_ACCEPT_CONTENT=['json', ],
#         CELERY_TASK_SERIALIZER='json',
#         CELERY_RESULT_SERIALIZER='json',
#     )
# else:
#     app.conf.update(
#         BROKER_URL='redis://localhost:6379/0',
#         CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
#         CELERY_RESULT_BACKEND='redis://localhost:6379/1',
#         CELERY_DISABLE_RATE_LIMITS=True,
#         CELERY_ACCEPT_CONTENT=['json', ],
#         CELERY_TASK_SERIALIZER='json',
#         CELERY_RESULT_SERIALIZER='json',


# # CELERY CONF
# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Baku'


