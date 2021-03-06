"""
Django settings for food-pantry project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url


from django.core.urlresolvers import reverse_lazy

from celery import Celery


LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+0)n1duej3viqqey^_9%nw5cwffhx0=6$xv0owtd@va4zqh#4o'

# SECURITY WARNING: don't run with debug turned on in production!

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


DEBUG = True

ALLOWED_HOSTS = ['*']





# Application definition

INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'django.contrib.admin',
    'shop',
    'cart',
    'orders',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'food-pantry.urls'

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

                # To be added per context processor (see page 233)n
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'food-pantry.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd44082qakjqosju',
        'USER': 'nqnjxsywzvnskt',
        'PASSWORD': 'a298d6f4992deac7df3bfbe1ad1b1243f4bfd034fe830d234f93c545df1b4daa',
        'HOST': 'postgres://nqnjxsywzvnskt:a298d6f4992deac7df3bfbe1ad1b1243f4bfd034fe830d234f93c545df1b4daa@ec2-174-129-193-169.compute-1.amazonaws.com:5432/d44082qakjqosj',
        'PORT': '5432',
    }
}




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# May need to drop the base_dir part...
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles', BASE_DIR, 'static/')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Added per page 274 for rendering PDFs, may not need?
# Will need to run collect static code on 275
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default'] = dj_database_url.config(default='postgres://nqnjxsywzvnskt:a298d6f4992deac7df3bfbe1ad1b1243f4bfd034fe830d234f93c545df1b4daa@ec2-174-129-193-169.compute-1.amazonaws.com:5432/d44082qakjqosj')

try:
    from .local_settings import *
except ImportError:
    pass

CART_SESSION_ID = 'cart'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# CELERY_BROKER_URL = 'amqp://localhost'

celery = Celery(broker="amqp://guest:guest@127.0.0.1:5672//")

celery.conf.update(
    CELERY_DEFAULT_QUEUE = "food-pantry",
    CELERY_DEFAULT_EXCHANGE = "food-pantry",
    CELERY_DEFAULT_EXCHANGE_TYPE = "direct",
    CELERY_DEFAULT_ROUTING_KEY = "food-pantry",
)

# https://www.pythonanywhere.com/forums/topic/54/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
