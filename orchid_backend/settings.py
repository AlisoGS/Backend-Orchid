import os
from pathlib import Path

import environ
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env((os.path.join(BASE_DIR, '.env')))
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')


AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

ALLOWED_HOSTS = ["*"]
AUTH_USER_MODEL = "core.Usuario"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "core",
    "rest_framework_simplejwt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "orchid_backend.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "orchid_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
     "default": {
        # default
        "ENGINE": "django.db.backends.postgresql",
        # database
        "NAME": env("PGDATABASE"),
        # pguser
        "USER": env("PGUSER"),
        # pgpass
        "PASSWORD": env("PGPASSWORD"),
        # pghost
        "HOST": env("PGHOST"),
        # pgport
        "PORT": env("PGPORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True



STATIC_URL = "static/"



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CORS_ALLOW_ALL_ORIGINS = True


STATIC_ROOT = os.path.join(BASE_DIR, "static")


REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     "rest_framework.permissions.DjangoModelPermissions",
    # ],
    # "DEFAULT_AUTHENTICATION_CLASSES": (
    #     "rest_framework_simplejwt.authentication.JWTAuthentication",
    # ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

}

SPECTACULAR_SETTINGS = {
    "TITLE": "Orchid API",
    "DESCRIPTION": "API para gerenciamento de Orchid, incluindo endpoints e a documentação.",
    "VERSION": "1.0.0",
}
