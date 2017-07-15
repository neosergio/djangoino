# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    log_text = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta(object):
        ordering = ["-datetime"]
        verbose_name_plural = "activities"
