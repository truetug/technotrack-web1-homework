# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
# Register your models here.
from categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    pass