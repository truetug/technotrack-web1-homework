# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = 'name', 'author',
    search_fields = 'name', 'author__username',
    list_filter = 'is_archive',