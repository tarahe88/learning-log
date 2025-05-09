"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # 20.2.8 为部署到heroku而修改wsgi.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

# application = get_wsgi_application()
application = Cling(get_wsgi_application()) # 20.2.8 为部署到heroku而修改wsgi.py