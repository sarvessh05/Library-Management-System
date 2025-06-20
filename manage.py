#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script is used to interact with the Django project via the command line.
It allows you to perform tasks such as running the server, applying migrations,
creating superusers, and more.
"""

import os  # Provides functions to interact with the operating system
import sys  # Provides access to system-specific parameters and functions


def main():
    """
    The main function that initializes Django's settings module
    and executes command-line arguments.
    """

    # Set the default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarymanagement.settings')

    try:
        # Import the Django command execution function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django is not installed or the virtual environment is not activated
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command-line arguments (e.g., runserver, migrate, createsuperuser)
    execute_from_command_line(sys.argv)


# Entry point of the script
if __name__ == '__main__':
    main()