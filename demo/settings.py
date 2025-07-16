import os
import socket

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

import environ  # type: ignore

# #######################
#   PROJECT DIRECTORIES
# #######################

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CONFIG_DIR)
DATABASE_DIR = os.path.join(ROOT_DIR, "data", "databases")
LOG_DIR = os.path.join(ROOT_DIR, "logs")

# ###############
#   ENVIRONMENT
# ###############

env = environ.Env()

environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))

DEBUG = env.bool("DJANGO_DEBUG", default=True)

# #####################
#   APPS & MIDDLEWARE
# #####################

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "ebird.api.data.apps.Config",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# ##############
#   WEB SERVER
# ##############

ROOT_URLCONF = "demo.urls"

WSGI_APPLICATION = "demo.wsgi.application"

if DEBUG:
    # From cookiecutter-django: We need to configure an IP address to
    # allow connections from, but in Docker we can't use 127.0.0.1 since
    # this runs in a container but we want to access the django_debug_toolbar
    # from our browser outside of the container.
    hostname, aliases, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]

# ############
#   DATABASE
# ############

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DB_NAME = env.str("DB_NAME", default="ebird_api_data")

DATABASES = {
    "default": env.db_url(default=f"sqlite:///{DATABASE_DIR}/{DB_NAME}.sqlite3")
}

# ############
#   SECURITY
# ############

SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="<not-set>")

# #############
#   TEMPLATES
# #############

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(CONFIG_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ########################
#   INTERNATIONALIZATION
# ########################

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English"))
]

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ################
#   STATIC FILES
# ################

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(CONFIG_DIR, "static"),
]

STATIC_URL = "/static/"

# ###########
#   LOGGING
# ###########

LOG_LEVEL = env.str("DJANGO_LOG_LEVEL", default="INFO")

if LOG_LEVEL not in ("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"):
    raise ImproperlyConfigured("Unknown level for logging: " + LOG_LEVEL)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "{asctime} [{levelname}] {message}",
            "style": "{",
            'datefmt': '%Y-%m-%d %H:%M',
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": os.path.join(LOG_DIR, "ebird-api-data.log"),
            "maxBytes": 1024 * 1024,
            "backupCount": 10,
        }
    },
    "loggers": {
        "django": {
            "level": "ERROR",
            "handlers": ["stdout"],
            "propagate": False,
        },
        "": {
            "handlers": ["stdout", "file"],
            "level": LOG_LEVEL,
        },
    },
}

# #####################
#   DJANGO EXTENSIONS
# #####################

SHELL_PLUS = "ipython"

GRAPH_MODELS = {
  'app_labels': ["data"],
}

# ####################
#   eBird API Data
# ####################

EBIRD_API_KEY = env.str("EBIRD_API_KEY")

# A dict mapping languages codes used by Django to locales used by eBird.
# This used to fetch data from the eBird taxonomy so the common, and family
# names for a species can be displayed in the local language.
EBIRD_LOCALES = env.json("EBIRD_LOCALES", '{"%s":"%s"}' % (LANGUAGE_CODE, LANGUAGE_CODE))
