from .base import *  # noqa: F403

ALLOWED_HOSTS = ['*']
DEBUG = True
INTERNAL_IPS = ('127.0.0.1', '192.168.56.2', '192.168.56.1', '192.168.56.2')

STATIC_ROOT = '/var/www/kqb_static/'
MEDIA_ROOT = '/var/www/kqb_media/'

WIKI_ACCOUNT_SIGNUP_ALLOWED = False