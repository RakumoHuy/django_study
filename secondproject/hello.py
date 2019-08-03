"""
WSGI config for secondproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.http import HttpResponse,Http404


def helloworld(request):
    message = "<html><body>Hello world</body></html>"
    from time import ctime
    return HttpResponse(ctime() + message, content_type='text/plain')
