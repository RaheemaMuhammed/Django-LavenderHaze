"""
Django settings for LavenderHaze project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%^lr13mv#ex9*a#lnv8-0(y9sb&qc#19(yqmar3tbhi5hw$5f0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['13.53.217.120', 'lavenderhaze.online']
CSRF_TRUSTED_ORIGINS = ['https://lavenderhaze.online']
CORS_ORIGIN_WHITELIST = ['https://lavenderhaze.online']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'category',
    'store',
    'carts',
    'orders',
    'adminpanel',
    'crispy_forms',
    
    
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

ROOT_URLCONF = 'LavenderHaze.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'LavenderHaze.wsgi.application'

AUTH_USER_MODEL =   'accounts.Account'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR /'static'
# STATICFILES_DIRS = [
#     'LavenderHaze/static',
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'LavenderHaze/static/')
]

# mediafiles configuration
MEDIA_URL   =   '/media/'
MEDIA_ROOT  =   BASE_DIR /'media'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

#SMTP CONFIGURATION
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='lavenderhaze107@gmail.com'
EMAIL_HOST_PASSWORD='pumpaergsbmcgerf'
EMAIL_USE_TLS=True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


#razorpay details
RAZOR_KEY_ID = 'rzp_test_ZPLCbNJUD304qL'

RAZOR_KEY_SECRET = 'MWpVlgeZ4eyuD5485MyKeSIB'

# Configure session engine
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
