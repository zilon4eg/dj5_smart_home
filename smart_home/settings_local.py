import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9m2%u2yq=+#)6c#^j7^1p+@mpiob-r)9ki+zrv%*ad779fz89l'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj5_smart_home',
        'USER': 'netology',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}