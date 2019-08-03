"""
WSGI config for secondproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render

def add_template(request):
    dic = {
        'title': 'index',
    }
    template = loader.get_template('first_template.html')
    return HttpResponse(template.render(dic))
