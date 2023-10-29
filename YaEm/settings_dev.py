import os
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

# environ
env = environ.Env(
    SECRET_KEY=str,
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")
# mutable variables
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}
# end mutable variables
INSTALLED_APPS = [
    # modern admin
    'jazzmin',
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
    'registration.apps.RegistrationConfig',
    # debug_toolbar
    "debug_toolbar",
    # translation
    "modeltranslation",
    # all auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.mailru',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # languages
    "django.middleware.locale.LocaleMiddleware",
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

ROOT_URLCONF = "YaEm.urls"

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
                # "context_processors.context_processors.cart_items_count",
            ],
        },
    },
]

WSGI_APPLICATION = "YaEm.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

if DEBUG:
    # static for dev
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/"),]
else:
    # static for prod
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# default redirect
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
# cookie time
SESSION_COOKIE_AGE = 604800
# cache lifetime (dev django, prod redis)
CACHES_LIFE_TIME = 60 * 15
# django all auth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP': {
#             'client_id': '201932057240-947a016k120mbef3tst1c9ujc11hm49g.apps.googleusercontent.com',
#             'secret': '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',
#             'key': ''
#         }
#     }
# }


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

# Celery settings
# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"


