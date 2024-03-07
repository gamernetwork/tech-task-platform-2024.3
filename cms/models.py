# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    slug = models.fields.SlugField()
    title = models.fields.CharField(max_length=1000)
    body = models.fields.TextField()

    def __str__(self):
      return self.title

# Create your models here.
