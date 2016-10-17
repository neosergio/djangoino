from django.contrib import admin
from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('log', 'datetime', 'user')

admin.site.register(Activity, ActivityAdmin)
