import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.what_the_health.settings")

application = get_wsgi_application()
