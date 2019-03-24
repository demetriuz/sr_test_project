# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class LevelType(models.Model):
    name = models.CharField(max_length=512, unique=True)
    is_internal = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Level(models.Model):
    type = models.ForeignKey(LevelType, on_delete=models.CASCADE)
    value = models.CharField(max_length=512)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('value', 'parent')

    def __str__(self):
        return f'{self.type} - {self.value}'


class Tag(models.Model):
    parent_level = models.ForeignKey(Level, on_delete=models.CASCADE)

    code = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
