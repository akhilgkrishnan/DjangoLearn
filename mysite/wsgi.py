"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
>>>>>>> 3f063ab310d1ebc253ad47a0e48dbbb6230293c0
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
