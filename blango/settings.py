from pathlib import Path
import os
from configurations import Configuration
from configurations import values
import dj_database_url
from datetime import timedelta

class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'
    DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io", "*"])
    INTERNAL_IPS = ["192.168.11.179"]
    AUTH_USER_MODEL = "blango_auth.User"
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    ACCOUNT_ACTIVATION_DAYS = 7
    SITE_ID = 1
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    }    
    MEDIA_ROOT = BASE_DIR/"media"
    MEDIA_URL = "/media/"

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'crispy_forms',
        'crispy_bootstrap5',
        'blango_auth',
        'blog',
        "debug_toolbar",
        "allauth", 
        "allauth.account", 
        "allauth.socialaccount", 
        "allauth.socialaccount.providers.google",
        "rest_framework",
        "rest_framework.authtoken",
        "drf_yasg",
        "django_filters",
        "versatileimagefield",
    ]
    
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
    
    ROOT_URLCONF = 'blango.urls'
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
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
    
    WSGI_APPLICATION = 'blango.wsgi.application'
    
    DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")
    
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]
    
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = values.Value("UTC")
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATIC_URL = '/static/'
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    
    X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
    CSRF_COOKIE_SAMESITE = None
    CSRF_TRUSTED_ORIGINS = [os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'
    
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} msg: {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }

    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
            "rest_framework_simplejwt.authentication.JWTAuthentication"
        ],
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticatedOrReadOnly"
        ],
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 100,
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend"
        ],
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend",
            "rest_framework.filters.OrderingFilter"
        ],


    }
    
    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
            "Basic": {"type": "basic"},
        }
    }

class Prod(Dev):
    DEBUG = False
    SECRET_KEY = values.SecretValue()


