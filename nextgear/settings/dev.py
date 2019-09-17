from .base import *

def require_env(name,default):
    value = os.getenv(name)
    if value is None:
        return default
    return value


# Set settings variables parsed from env
SECRET_KEY = require_env('SECRET_KEY','*k88^mjs!#0tq&xm@_qvrq%(y$&eiaye6l6jmw65ugeq_e_@v)')
DEBUG = bool(require_env('DEBUG', 'True'))
SITE_ID = require_env('SITE_DOMAIN','localhost')

# It is insecure I know
ALLOWED_HOSTS =  eval(require_env('ALLOWED_HOSTS','["localhost","127.0.0.1"]'),{"__builtins__":None},{})


# Database settings
DATABASES = {
    'default': {}}

DATABASES['default'] = dj_database_url.config(conn_max_age=600,default='sqlite://./db.sqlite3')
