from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    log = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        ordering = ['-datetime']
        verbose_name_plural = 'activities'
