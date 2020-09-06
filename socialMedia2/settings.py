"""
Django settings for socialMedia2 project.
Generated by 'django-admin startproject' using Django 2.2.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# remember on same level as manage.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '3y0rw-13=7-_@a1lvp198g6w_ivf@*r+c997z2g%zg15hk3d8m'
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '3y0rw-13=7-_@a1lvp198g6w_ivf@*r+c997z2g%zg15hk3d8m')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'social-media-michal.herokuapp.com']
LOGIN_URL = "/login"

MAX_POST_LENGTH = 240
POST_ACTION_OPTIONS = ["like", "unlike", "repost"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party
    'corsheaders',
    'rest_framework',
    # internal
    'profiles',
    'posts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'socialMedia2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'socialMedia2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yzxparmq',
        'USER': 'yzxparmq',
        'PASSWORD': 'hpyz6aZNZ8C3L-Fl9U0Q1m-D0USttd9B',
        'HOST': 'rogue.db.elephantsql.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static-root")


CORS_ORIGIN_ALLOW_ALL = True # any website has access to my api
CORS_URLS_REGEX = r'^/api/.*$'


DEFAULT_RENDERER_CLASSES = [
        'rest_framework.renderers.JSONRenderer',
    ]

DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.SessionAuthentication'
]
if DEBUG:
    DEFAULT_RENDERER_CLASSES += [
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
    # DEFAULT_AUTHENTICATION_CLASSES += [
    #     'socialMedia2.rest_api.dev.DevAuthentication'
    # ]
REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': DEFAULT_AUTHENTICATION_CLASSES,
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
}



# """
# Django settings for socialMedia2 project.

# Generated by 'django-admin startproject' using Django 2.2.14.

# For more information on this file, see
# https://docs.djangoproject.com/en/2.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/2.2/ref/settings/
# """

# import os
# from corsheaders.defaults import default_headers

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '3y0rw-13=7-_@a1lvp198g6w_ivf@*r+c997z2g%zg15hk3d8m'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', '.cfe.sh', 'localhost', ]
# LOGIN_URL = "/login"
# CORS_ORIGIN_ALLOW_ALL = True
# MAX_POST_LENGTH = 240
# POST_ACTION_OPTIONS = ["like", "unlike", "repost"]

# APPEND_SLASH = True

# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'corsheaders',
#     'rest_framework',
#     'posts',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# CORS_ALLOWED_ORIGINS = [
# "http://localhost:3000",
# "http://localhost:8000",
# '127.0.0.1', 
# '.cfe.sh', 
# 'localhost', 
# "http://192.168.1.17:3000",
# "http://127.0.0.1:8000"
# ]

# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'x-csrf-token',
#     'x-requested-with'
# ]


# ROOT_URLCONF = 'socialMedia2.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [ os.path.join(BASE_DIR,"templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'socialMedia2.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'yzxparmq',
#         'USER': 'yzxparmq',
#         'PASSWORD': 'hpyz6aZNZ8C3L-Fl9U0Q1m-D0USttd9B',
#         'HOST': 'rogue.db.elephantsql.com',
#         'PORT': '5432',
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
# ]

# STATIC_ROOT = os.path.join(BASE_DIR,"static-root")

# CORS_ORIGIN_ALLOW_ALL = True

# CORS_URLS_REGEX = r'^/api/.*$'

# DEFAULT_RENDERER_CLASSES = [
#         'rest_framework.renderers.JSONRenderer',
#     ]

# DEFAULT_AUTHENTICATION_CLASSES = [
#     'rest_framework.authentication.SessionAuthentication'
# ]
# if DEBUG:
#     DEFAULT_RENDERER_CLASSES += [
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ]
#     DEFAULT_AUTHENTICATION_CLASSES += [
#         'socialMedia2.rest_api.dev.DevAuthentication'
#     ]
# REST_FRAMEWORK = {
    
#     'DEFAULT_AUTHENTICATION_CLASSES': DEFAULT_AUTHENTICATION_CLASSES,
#     'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
# }