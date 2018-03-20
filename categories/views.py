# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, reverse

from categories.models import Category


def categories_list(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'categories/categories_list.html', context)
    # return HttpResponse('This is list of categories')


def category_detail(request, pk=None):

    category = Category.objects.get(id=pk)

    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False)
    }
    return render(request, 'categories/category_detail.html', context)
    # return HttpResponse('This is category {}'.format(category_id))
