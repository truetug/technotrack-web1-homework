# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(OldUserAdmin):

    pass
