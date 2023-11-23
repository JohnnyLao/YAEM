from Yaem.settings_dev import *

# debug for prod
DEBUG = False
# hosts for prod
ALLOWED_HOSTS = ['yaem.kz', 'www.yaem.kz']
# redis cache settings only prod
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#     }
# }
# postgresql for prod
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
