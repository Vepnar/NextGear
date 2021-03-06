#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

dev = True

def main():

    # Default environ
    default_settings = {
            'SECRET_KEY': '*k88^mjs!#0tq&xm@_qvrq%(y$&eiaye6l6jmw65ugeq_e_@v)',
            'DJANGO_SETTINGS_MODULE' : 'nextgear.settings.staging',
            'DEBUG' : 'True',
            'SITE_DOMAIN' : 'localhost',
            'ALLOWED_HOSTS' : '[\'127.0.0.1\']'
    }
    if dev:
        default_settings = {
            'DJANGO_SETTINGS_MODULE' : 'nextgear.settings.dev',
    }

    # Set default environ
    for key, value in default_settings.items():
        os.environ.setdefault(key, value)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
