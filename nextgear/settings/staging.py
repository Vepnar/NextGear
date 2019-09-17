from .base import *

def require_env(name):
    # Raise an error if the environment variable isn't defined
    value = os.getenv(name)
    if value is None:
        raise ImproperlyConfigured(f'Required environment variable "{name}" is not set.')
    return value


# Set settings variables parsed from env
SECRET_KEY = require_env('SECRET_KEY')
DEBUG = bool(require_env('DEBUG'))
SITE_ID = require_env('SITE_DOMAIN')

# It is insecure I know
ALLOWED_HOSTS =  eval(require_env('ALLOWED_HOSTS'),{"__builtins__":None},{})


# Database settings
DATABASES = {
    'default': {}}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)