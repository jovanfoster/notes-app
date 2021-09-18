from ._base import *

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '$fk1ru#!v8&81_8qkn&@k%uqu1^&_t+utmddvr3nr)4lpsi-63')

ALLOWED_HOSTS = ['django-notes-app-09-21.herokuapp.com']

import dj_database_url 
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    (os.path.join(BASE_DIR, 'static')), 
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
