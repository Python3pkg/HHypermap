

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celeryapp import app as celery_app  # noqa

__version__ = '0.3.11'
__description__ = 'hhypermap'
