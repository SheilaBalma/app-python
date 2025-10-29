from pathlib import Path
import os
from dotenv import load_dotenv

# === BASE ===
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")  # opcional, para variables locales

SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

# === APPS ===
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "clima",
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ WhiteNoise acá
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === URLS / WSGI ===
ROOT_URLCONF = "apppython.urls"
WSGI_APPLICATION = "apppython.wsgi.application"

# === TEMPLATES ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # carpeta global de templates
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

# === DATABASE ===
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# === ARCHIVOS ESTÁTICOS ===
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "clima" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# === SEGURIDAD (Render) ===
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ["https://*.onrender.com"]

# === INTERNACIONALIZACIÓN ===
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Buenos_Aires"

# === CACHÉ (para respuestas de API) ===
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    }
}
