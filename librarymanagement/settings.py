import os
from pathlib import Path

# ---------------- BASE SETTINGS ---------------- #

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# ---------------- SECURITY ---------------- #

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'k(6-_4sgig$sbrccr2*0=7s)bklpiywi#_121l)s(f8)dq^^wv')

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['*']  # Or ['your-app-name.onrender.com']

# ---------------- INSTALLED APPS ---------------- #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',
]

# ---------------- MIDDLEWARE ---------------- #

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------- URL & WSGI ---------------- #

ROOT_URLCONF = 'librarymanagement.urls'
WSGI_APPLICATION = 'librarymanagement.wsgi.application'

# ---------------- TEMPLATES ---------------- #

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ---------------- DATABASE ---------------- #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ---------------- PASSWORD VALIDATION ---------------- #

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------- INTERNATIONALIZATION ---------------- #

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------- STATIC FILES ---------------- #

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]

# Important for production on Render:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ---------------- LOGIN REDIRECT ---------------- #

LOGIN_REDIRECT_URL = '/afterlogin'

# ---------------- EMAIL SETTINGS ---------------- #

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

# ---------------- RENDER DEPLOYMENT HINTS ---------------- #

# Optional future: Set this if using PostgreSQL on Render
# import dj_database_url
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)