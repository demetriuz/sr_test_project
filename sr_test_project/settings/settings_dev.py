from .settings import *

INSTALLED_APPS += [
    'django_extensions',
]

MIDDLEWARE += ['querycount.middleware.QueryCountMiddleware']
QUERYCOUNT = {
    'THRESHOLDS': {
        'MEDIUM': 2,
        'HIGH': 5,
        'MIN_TIME_TO_LOG': 0,
        'MIN_QUERY_COUNT_TO_LOG': 0
    },
    'IGNORE_REQUEST_PATTERNS': [],
    'IGNORE_SQL_PATTERNS': [],
    'DISPLAY_DUPLICATES': 2,
    'RESPONSE_HEADER': 'X-DjangoQueryCount-Count'
}
