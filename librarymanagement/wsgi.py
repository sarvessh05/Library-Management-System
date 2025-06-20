"""
WSGI config for librarymanagement project.

This script is responsible for serving the Django application using WSGI.

It exposes the WSGI callable as a module-level variable named ``application``.

For more details, see:
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'librarymanagement' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarymanagement.settings')

# Get the WSGI application object for the project
application = get_wsgi_application()