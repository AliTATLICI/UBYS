from UBYS.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ubys',
        'USER': 'user',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
