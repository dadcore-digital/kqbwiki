from .base import *  # noqa: F403

ALLOWED_HOSTS = [
    'killerqueenblack.wiki',
    'kqb.pythonanywhere.com',
    'wiki.killerqueenblack.com'
]

DEBUG = False


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kqbwiki',
        'USER': 'kqbwiki',
        'PASSWORD': get_secret('DB_PASSWORD'),  # noqa: F405
        'HOST': '',
        'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB'
        }
    }
}

STATIC_ROOT = '/home/ianfitzpatrick/apps/kqbwiki_static'
MEDIA_ROOT = '/home/ianfitzpatrick/apps/kqbwiki_media'


WIKI_ACCOUNT_SIGNUP_ALLOWED = False