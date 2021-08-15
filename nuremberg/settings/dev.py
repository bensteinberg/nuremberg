import os
from .generic import *

SECRET_KEY = '@xf59!g4b(=z==*@#(0hdjc$_q5taw-t-1m#9@o!nzx_h1z@r9'
DEBUG = True
COMPRESS_ENABLED = False
DATABASES['default'] = {
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'nuremberg_dev',
  'USER': 'nuremberg',
  'HOST': 'localhost',
}
if os.environ.get('DOCKERIZED'):
    DATABASES['default']['HOST'] = 'db'

HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'ENGINE': 'nuremberg.search.lib.solr_grouping_backend.GroupedSolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/nuremberg_dev'
    },
}
if os.environ.get('DOCKERIZED'):
    HAYSTACK_CONNECTIONS['default']['URL'] = 'http://solr:8983/solr/nuremberg_dev'

# this can be used to index a local db to a remote Solr instance
if os.environ.get('SOLR_REMOTE'):
    HAYSTACK_CONNECTIONS['default']['URL'] = os.environ.get('SOLR_REMOTE')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.LESS', {
      "executable": "lessc",
      "sourcemap_enabled": True,
    }),
)

# MIDDLEWARE_CLASSES.append('django_cprofile_middleware.middleware.ProfilerMiddleware')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
