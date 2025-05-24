from pathlib import Path
from decouple import Config, RepositoryEnv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.getenv('ENV', 'local')

ENV_FILE_PATH = os.path.join(BASE_DIR, 'envs', f'.env.{ENV}') # Ruta completa al archivo .env según el entorno

print("DEBUG FROM CONFIG =", ENV_FILE_PATH)

config = Config(RepositoryEnv(ENV_FILE_PATH)) # AutoConfig

print("DEBUG FROM CONFIG =", config('DB_PORT'))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'rest_framework', # Dependencia necesaria para poder construir APIs Rest full
    'users',
    'brands'
]

MIDDLEWARE = [
    'middlewares.jwt_auth.JWTAuthenticationMiddleware'
]

ROOT_URLCONF = 'ecomerce_django.urls'

WSGI_APPLICATION = 'ecomerce_django.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}

APPEND_SLASH = True