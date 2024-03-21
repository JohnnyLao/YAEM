import os
from datetime import timedelta
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    SECRET_KEY=(
        str,
        'django-insecure-s!asdatxswfgdrt*i+gwgxl9i2jh1fo(-a8yf8%)e3(-*5z(xd_',
    ),
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(list, ['localhost', '127.0.0.1']),
    # postgres
    SQL_ENGINE=(str, 'django.db.backends.sqlite3'),
    POSTGRES_DB=(str, os.path.join(BASE_DIR, "db.sqlite3")),
    POSTGRES_USER=(str, 'root'),
    POSTGRES_PASSWORD=(str, 'password'),
    POSTGRES_HOST=(str, 'localhost'),
    POSTGRES_PORT=(str, '5432'),
    # minio
    MINIO_ROOT_USER=str,
    MINIO_ROOT_PASSWORD=str,
    MINIO_BUCKET_NAME=str,
    MINIO_ENDPOINT=str,
)

environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

INSTALLED_APPS = [
    # modern admin
    "jazzmin",
    # default django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.template",
    "django.contrib.humanize",
    # my app
    "main.apps.MainConfig",
    "partner.apps.PartnerConfig",
    "cart.apps.CartConfig",
    "banquets.apps.BanquetsConfig",
    'users.apps.UsersConfig',
    # debug_toolbar
    "debug_toolbar",
    'phonenumber_field',
    # translation
    "modeltranslation",
    # swagger
    "drf_spectacular",
    # django rest
    "rest_framework",
    # cors
    "corsheaders",
    # all auth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # languages
    "django.middleware.locale.LocaleMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # all auth
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "Yaem.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "context_processors.context_processors.data_counter_site",
                "context_processors.context_processors.get_total_cart_sum",
            ],
        },
    },
]

WSGI_APPLICATION = "Yaem.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "ru"
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

if DEBUG:
    # static for dev
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static/"),
    ]
else:
    # static for prod
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# default redirect
LOGOUT_REDIRECT_URL = "/"
# cookie time
SESSION_COOKIE_AGE = 86400
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# cache lifetime (dev django, prod redis)
CACHES_LIFE_TIME = 0
AUTH_USER_MODEL = 'users.User'

# languages
LANGUAGES = [
    ("ru", _("Russian")),
    ("en", _("English")),
    ("kk", _("Kazakh")),
]
LOCALE_PATHS = [
    BASE_DIR / "locale",
]
# model translation
MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
MODELTRANSLATION_LANGUAGES = ("ru", "en", "kk")

# debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# jazzmin config ui
JAZZMIN_UI_TWEAKS = {
    "theme": "litera",
}
JAZZMIN_SETTINGS = {
    "topmenu_links": [
        {
            "name": "Админ-панель",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Главная",
            "url": "main:main_page",
            "new_window": True,
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Партнерка",
            "url": "partner:partner_page",
            "new_window": True,
            "permissions": ["auth.view_user"],
        },
    ],
    "usermenu_links": [
        {
            "name": "Открыть сайт",
            "url": "main:main_page",
            "permissions": ["auth.view_user"],
        },
    ],
}

#########################
# DJANGO REST FRAMEWORK
#########################
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAdminUser",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "api_v1.utils.pagination.BasePagination",
}

ACCESS_TOKEN_LIFETIME = timedelta(hours=1)
REFRESH_TOKEN_LIFETIME = timedelta(days=30)
#########################

########################
# DRF SPECTACULAR
########################
SPECTACULAR_SETTINGS = {
    "TITLE": "YAEM API",
    "DESCRIPTION": "Documentation for YAEM API",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.AllowAny",
    ],
    "SERVE_AUTHENTICATION": [
        "rest_framework.authentication.BasicAuthentication",
    ],
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayOperationId": True,
        "syntaxHighlight.active": True,
        "syntaxHighlight.theme": "arta",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "filter": True,
        "requestSnippetsEnabled": True,
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "SORT_OPERATIONS": False,
    "ENABLE_DJANGO_DEPLOY_CHECK": False,
    "DISABLE_ERRORS_AND_WARNINGS": True,
}
########################

######################
# CORS HEADERS
######################
CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:5173', 'http://127.0.0.1:8000']
CORS_ALLOW_HEADERS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = False

# django-storages settings
# if not DEBUG:
#     DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
#
#     MINIO_ACCESS_KEY = env("MINIO_ROOT_USER")
#     MINIO_SECRET_KEY = env("MINIO_ROOT_PASSWORD")
#     MINIO_BUCKET_NAME = env("MINIO_BUCKET_NAME")
#     MINIO_ENDPOINT = env("MINIO_ENDPOINT")
#
#     AWS_ACCESS_KEY_ID = MINIO_ACCESS_KEY
#     AWS_SECRET_ACCESS_KEY = MINIO_SECRET_KEY
#     AWS_STORAGE_BUCKET_NAME = MINIO_BUCKET_NAME
#     AWS_S3_ENDPOINT_URL = MINIO_ENDPOINT
#     AWS_DEFAULT_ACL = None
#     AWS_QUERYSTRING_AUTH = True
#     AWS_S3_FILE_OVERWRITE = False
