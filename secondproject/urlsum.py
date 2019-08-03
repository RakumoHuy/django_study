"""
WSGI config for secondproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.http import HttpResponse


def url_sum(request,a,b):
    a_int = int(a,10)
    b_int = int(b,10)
    return HttpResponse(str(a_int+b_int), content_type='text/plain')
