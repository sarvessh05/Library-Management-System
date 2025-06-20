"""
ASGI config for librarymanagement project.

This file sets up the ASGI application used for handling asynchronous requests.
It exposes the ASGI callable as a module-level variable named `application`.

For more details, see:
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# 🔹 Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarymanagement.settings')

# 🔹 Create and expose the ASGI application instance
application = get_asgi_application()