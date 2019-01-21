# -*- coding: utf8 -*-

"""
    OParoquiano - Solução completa que tem por objetivo ajudar as paroquias,
    capelas, igrejas, dioceses a divulgar suas atividades para comunidade
    local e da região por meio de um sistema web + app android.

    Copyright (C) 2019 - Luis Vitório

    Este programa é um software livre: você pode redistribuí-lo e/ou
    modificá-lo sob os termos da Licença Pública Geral Affero GNU,
    conforme publicado pela Free Software Foundation, seja a versão 3
    da Licença ou (a seu critério) qualquer versão posterior.

    Este programa é distribuído na esperança de que seja útil,
    mas SEM QUALQUER GARANTIA; sem a garantia implícita de
    COMERCIALIZAÇÃO OU ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Veja a
    Licença Pública Geral Affero GNU para obter mais detalhes.

    Você deve ter recebido uma cópia da Licença Pública Geral Affero GNU
    junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

    linkedin: https://www.linkedin.com/in/vitorioluis/
    email: vitorioluis@gmail.com

"""



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_4&#&_1qs&o%-=mlt6^1f%4)27gqt)o%ql^723udc46s-x@8ys'

# SECUaRITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Allow all host headers
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # libs
    'bootstrap3',

    # apps
    'oparoquiano.accounts',
    'oparoquiano.core',
    'oparoquiano.agenda',
    'oparoquiano.paroquia',
    'oparoquiano.api',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

ROOT_URLCONF = 'oparoquiano.urls'
WSGI_APPLICATION = 'oparoquiano.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'oparoquiano/core/static'
#STATIC_ROOT = os.path.join(BASE_DIR, 'oparoquiano/core', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'oparoquiano','media')

# Email
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'nome@gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'email@gmail.com'
# EMAIL_HOST_PASSWORD = '******'
# EMAIL_PORT = 587

# CONTACT_EMAIL=''

# Auth
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_URL = 'accounts:logout'
AUTH_USER_MODEL = 'accounts.User'

URL_RAIZ = 'http://localhost:8000/'
SITE = URL_RAIZ

LOGO_PADRAO = 'NoImg.png'

# Sessao
SESSION_COOKIE_AGE = 1200  # tempo para expirar a pagina caso nao haja atividade
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # sessao aberta enquanto o navegador estiver aberto
SESSION_SAVE_EVERY_REQUEST = True  # sessao seja renovada a cada requisicao

# mariadb
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DATABASE',
#         'USER': 'root',
#         'PASSWORD': 'SENHA',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'autocommit': True,
#             'sql_mode': 'traditional',
#         },
#     }
# }


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oparoquiano.db'),
    }
}
