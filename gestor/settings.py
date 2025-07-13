from pathlib import Path

# BASE_DIR es la carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'tu-clave-secreta-aqui'
DEBUG = True
ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'libros',  # Asegúrate de que esté el nombre de tu app aquí
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal
ROOT_URLCONF = 'gestor.urls'

# Plantillas
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Apunta a la carpeta 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {  # Aquí aseguramos que 'OPTIONS' esté bien definido
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'gestor.wsgi.application'

# Base de datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# En tu archivo settings.py

# ... otras configuraciones...

# Configuración de seguridad para CSRF
CSRF_COOKIE_SECURE = False  # Para desarrollo local, debe ser False
CSRF_COOKIE_HTTPONLY = False  # Permite que el token sea accesible desde el navegador
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',  # Asegúrate de incluir localhost y 127.0.0.1
    'http://localhost',
]

SESSION_COOKIE_SECURE = False  # Para desarrollo local, debe ser False

# ... otras configuraciones...

# Validación de contraseñas
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

# Configuración regional
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Asuncion'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Directorio de archivos estáticos
]

# Archivos multimedia (PDFs, imágenes subidas)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Directorio donde se guardarán los archivos de medios

# Campo por defecto para IDs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Mostrar errores detallados en el navegador (solo en desarrollo)
DEBUG_PROPAGATE_EXCEPTIONS = True
