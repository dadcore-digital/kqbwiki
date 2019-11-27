import json
from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured


# Private Key Settings: (Store all sensitive keys/other data for settings
# files outside version control)
cwd = os.path.dirname(os.path.realpath(__file__))
with open('%s/secrets.json' % cwd) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """
    Get secret variable or return explicit exception.

    Always return as string, not unicode.

    Must store this in base settings file due to structure of multiple
    settings files, or risk circular imports.
    """
    try:
        return str(secrets[setting])

    except KeyError:
        error_msg = "Missing %s setting from secrets file" % setting
        raise ImproperlyConfigured(error_msg)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
TEMPLATE_DIR = str(Path(BASE_DIR).parents[1]) + '/templates'

SECRET_KEY = get_secret('SECRET_KEY')
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.humanize.apps.HumanizeConfig',
    'django_nyt.apps.DjangoNytConfig',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki.apps.WikiConfig',
    'wiki.plugins.attachments.apps.AttachmentsConfig',
    'wiki.plugins.notifications.apps.NotificationsConfig',
    'wiki.plugins.images.apps.ImagesConfig',
    'wiki.plugins.links.apps.LinksConfig',
    'wiki.plugins.help.apps.HelpConfig',
    'wiki.plugins.macros.apps.MacrosConfig',
    'wiki.plugins.globalhistory.apps.GlobalHistoryConfig',
    'kqbwiki',
    'django_extensions',

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

ROOT_URLCONF = 'kqbwiki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai'

            ],
        },
    },
]

WSGI_APPLICATION = 'kqbwiki.wsgi.application'

SITE_ID = 1

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kqbwiki',
        'USER': 'kqbwiki',
        'PASSWORD': get_secret('DB_PASSWORD'),  # noqa: F405
        'HOST': '127.0.0.1',
        'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB'
        }
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# DJango Wiki Settings
WIKI_MARKDOWN_HTML_STYLES = [
    'width', 'height', 'size', 'padding', 'margin', 'border', 'float',
    'display', 'max-width', 'min-width'
]
