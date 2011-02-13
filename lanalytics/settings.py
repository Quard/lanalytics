import logging
import os


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/../db-%s.db' % (PROJECT_ROOT, PROJECT_NAME),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static_media')
MEDIA_URL = '/media/'

STATIC_ROOT = MEDIA_ROOT
STATIC_URL = MEDIA_URL
STATICFILES_PREPEND_LABEL_APPS = (
    'django.contrib.admin',
)

ADMIN_MEDIA_PREFIX = '/media/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5z(l7tamdixlyzas4tdto%7bs5%s9_!-4o6f2*#@=8g=8zdg8_'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'devserver.middleware.DevServerMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = '%s.urls' % (PROJECT_NAME,)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    # common
    'devserver',
    'staticmedia',
    'compress',
    'google_analytics',

    # additional, keep project's namespace

)

GOOGLE_ANALYTICS_MODEL = True

if not DEBUG:
    CACHE_BACKEND = 'locmem://'

# import common settings
from common_settings import *

try:
    from settings_local import *
except ImportError:
    logging.error("Can't import settings_local'")
