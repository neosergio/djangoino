# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Activity

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("datetime", "log_text", "user")

admin.site.register(Activity, ActivityAdmin)
