"""
Django settings for lp_electric project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from datetime import datetime
from collections import OrderedDict

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p14kp-pivn-_tfqsq$&3^v#dku!p2bz14=l_m9chqih$jf6o3&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# http://bit.ly/sorl-thumbnail-docs
THUMBNAIL_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin.apps.SimpleAdminConfig',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'mptt',
    'widget_tweaks',
    'sorl.thumbnail',
    'images',
    'pages',
    'catalog',
    'lp_electric',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lp_electric.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lp_electric.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'front'),
    ASSETS_DIR,
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOCALHOST = 'http://127.0.0.1:8000/'
BASE_URL = 'https://127.0.0.1'

PLACEHOLDER_IMAGE = 'images/common/logo.svg'
PLACEHOLDER_ALT = 'Логотип компании Hoffman Electric LP'

# For sitemaps and sites framework
SITE_ID = 1
SITE_DOMAIN_NAME = '127.0.0.1:8000'

# Autocomplete and search settings
SEARCH_SEE_ALL_LABEL = 'Смотреть все результаты'

SITE_CREATED = datetime(year=2016, month=10, day=25)

# Some defaults for autocreation struct pages: index, catalog tree
# Pages with this data are created in DB only once.
CUSTOM_PAGES = {
    'index': {
        'slug': 'index',
        '_title': 'LP Electric',
        'h1': 'LP Electric',
        '_menu_title': 'Главная',
        'date_published': SITE_CREATED,
    },
    'category_tree': {
        'slug': 'category_tree',
        '_title': 'Каталог товаров',
        'h1': 'Каталог товаров',
        '_menu_title': 'Каталог',
        'date_published': SITE_CREATED,
    },
    'search': {
        'slug': 'search',
        '_title': 'Результаты поиска',
        'h1': 'Результаты поиска',
        'date_published': SITE_CREATED,
    },
    'jobs': {
        'slug': 'jobs',
        '_title': 'Вакансии',
        'h1': 'Вакансии',
        '_menu_title': 'Вакансии',
        'date_published': SITE_CREATED,
    },
}

# Some defaults for autocreation struct pages: index, catalog tree
# Pages with this data are created in DB only once.
FLAT_PAGES = {
    'proger': {
        'slug': 'proger',
        '_title': 'Прогер',
        'h1': 'Прогер',
        '_menu_title': 'Прогер',
        'date_published': SITE_CREATED,
        'parent': 'jobs',
    },
    'seller': {
        'slug': 'seller',
        '_title': 'Продавец-консультант',
        'h1': 'Продавец-консультант',
        '_menu_title': 'Продавец-консультант',
        'date_published': SITE_CREATED,
        'parent': 'jobs',
    },
    'about': {
        'slug': 'about',
        '_title': 'О нас',
        'h1': 'О нас',
        '_menu_title': 'О нас',
        'date_published': SITE_CREATED,
    },
    'contacts': {
        'slug': 'contacts',
        '_title': 'Контакты',
        'h1': 'Контакты',
        'date_published': SITE_CREATED,
    },
    'conditions': {
        'slug': 'conditions',
        '_title': 'Условия работы',
        'h1': 'Условия работы',
        '_menu_title': 'Условия работы',
        'date_published': SITE_CREATED,
    },
    'shipment': {
        'slug': 'shipment',
        '_title': 'Доставка',
        'h1': 'Доставка',
        '_menu_title': 'Доставка',
        'date_published': SITE_CREATED,
    },
    'support': {
        'slug': 'support',
        '_title': 'Поддержка',
        'h1': 'Поддержка',
        '_menu_title': 'Поддержка',
        'date_published': SITE_CREATED,
    },
}

# Custom categories for autocreation with data migrations.
# We need OrderedDict here because of 'parent' key on child items
CATEGORIES = OrderedDict([
    ('kitchen', {
        'slug': 'index',
        'name': 'Кухня',
        'position': 0,
    }),
    ('coffee_makers', {
        'slug': 'coffee-makers',
        'name': 'Кофеварки',
        'parent': 'kitchen',
        'position': 0,
    }),
    ('mixers', {
        'slug': 'mixers',
        'name': 'Миксеры',
        'parent': 'kitchen',
        'position': 1,
    }),
    ('juicers', {
        'slug': 'juicers',
        'name': 'Соковыжималки',
        'parent': 'kitchen',
        'position': 2,
    }),
    ('house', {
        'slug': 'house',
        'name': 'Дом',
        'position': 1,
    }),
    ('irons', {
        'slug': 'irons',
        'name': 'Утюги',
        'parent': 'house',
        'position': 0,
    }),
    ('libra', {
        'slug': 'libra',
        'name': 'Весы',
        'parent': 'house',
        'position': 1,
    }),
    ('vacuum_cleaners', {
        'slug': 'vacuum-cleaners',
        'name': 'Пылесосы',
        'parent': 'house',
        'position': 2,
    }),
    ('climate', {
        'slug': 'climate',
        'name': 'Климат',
        'position': 2,
    }),
    ('accessories', {
        'slug': 'accessories',
        'name': 'Аксессуары',
        'position': 3,
    }),
])
