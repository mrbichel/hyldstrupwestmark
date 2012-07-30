# coding=utf-8
import os.path
import sys
import platform

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_URLCONF = 'hyldstrupwestmark.urls'

sys.path.append(BASE_PATH + '/apps')

PRODUCTION_HOSTNAME = "tango"

ADMINS = (
    ('Johan Bichel Lindegaard', 'sysadmin@tango.johan.cc'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "noreply@hyldstrupwestmark.com"

DEVELOPMENT_MODE = (platform.node() != PRODUCTION_HOSTNAME)
if DEVELOPMENT_MODE:
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    DEBUG = False
    MEDIA_URL = 'http://media.hyldstrupwestmark.johan.cc/'
    STATIC_URL = 'http://static.hyldstrupwestmark.johan.cc/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

TEMPLATE_DEBUG = DEBUG

# Static files
MEDIA_ROOT = BASE_PATH + '/../static/uploads'
STATICFILES_DIRS = (
    BASE_PATH + '/../static',
)

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'en_UK'
SITE_ID = 1
USE_I18N = True
USE_L10N = False


TIME_FORMAT = "H:i"
SHORT_DATETIME_FORMAT = 'm/d/Y H:i'
DATETIME_FORMAT	= 'N j, Y, H:i'


GRAPPELLI_ADMIN_TITLE = "Hyldstrup & Westmark"
GRAPPELLI_INDEX_DASHBOARD = 'hyldstrupwestmark.dashboard.CustomIndexDashboard'


LOCALE_PATHS = (
    BASE_PATH + '/locale',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_DIRS = (
    BASE_PATH + '/templates/'
)

INSTALLED_APPS = (

    'courses',

    'south',
    'sorl.thumbnail',
    'flatblocks',
    'grappelli.dashboard',
    'grappelli',
    'debug_toolbar',
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.flatpages',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INTERNAL_IPS = ('127.0.0.1',)


try:
    execfile(BASE_PATH + '/settings_local.py')
except IOError:
    sys.stderr.write("\nYou need to copy settings_local.example to settings_local.py and customize it.\n")
    sys.exit(1)