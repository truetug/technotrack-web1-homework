# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):

    name = request.GET.get('name')
    return HttpResponse('Hello {}'.format(name))

