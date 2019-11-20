from .base import *  # noqa: F403

ALLOWED_HOSTS = ['killerqueenblack.wiki']
DEBUG = False


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kqbwiki',
        'USER': 'kqb',
        'PASSWORD': get_secret('DB_PASSWORD'),  # noqa: F405
        'HOST': 'kqb.mysql.pythonanywhere-services.com',
        'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB'
        }
    }
}