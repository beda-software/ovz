# -*- coding: utf-8 -*-
# Global settings for ovz project.

from os.path import abspath, dirname, basename, join, split

MAIN_APPS_PATH = abspath(dirname(__file__))
MAIN_APPS_NAME = basename(MAIN_APPS_PATH)
PROJECT_PATH = split(MAIN_APPS_PATH)[0]
PROJECT_NAME = basename(PROJECT_PATH)

BREADCRUMBS_AUTO_HOME = True
BREADCRUMBS_HOME_TITLE = u'Главная'

FILE_UPLOAD_PERMISSIONS = 0644

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

TIME_ZONE = 'Asia/Krasnoyarsk'
LANGUAGE_CODE = 'RU-ru'
USE_I18N = True
USE_L10N = True

STATIC_ROOT = join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL
MEDIA_ROOT = join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = join(MEDIA_ROOT, 'ckupload')
STATICFILES_DIRS = ()
TEMPLATE_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware'
)

ANONYMOUS_USER_ID = -1
SITE_ID = 1
SECRET_KEY = 'x0x8--)5qz7qyiv71v-*fw7(_kz(^4mzdj6ugimuon@jt#@9%p'
ROOT_URLCONF = 'ovz.urls'
WSGI_APPLICATION = 'ovz.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'breadcrumbs',

    'south',
    'ckeditor',
    'sorl.thumbnail',
)

LOCAL_APPS = (
    'main',
    'play_and_learn',
    'guest',
    'methodical_bank',
    'your_choice',
    'schools',
)

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Format'], ['Undo', 'Redo'],
            ['Bold', 'Italic', 'Underline'],
            ['Link', 'Unlink'],
            ['BulletedList', 'NumberedList', 'HorizontalRule'],
            ['Cut', 'Copy', 'Paste'],
            ['Source', 'Maximize'],
        ],
        'defaultLanguage': 'en',
        'uiColor': '#FAFAFA',
        'language': 'fr'
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

for item in LOCAL_APPS:
    INSTALLED_APPS += (item,)
    TEMPLATE_DIRS += (join(PROJECT_PATH, item, 'templates'),)
    STATICFILES_DIRS += ((item, join(PROJECT_PATH, item, 'static')),)

from local import *
