# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from . import models as m


class CategoryAdmin(admin.ModelAdmin):
    pass


class AttrAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(m.LevelType, CategoryAdmin)
admin.site.register(m.Level, AttrAdmin)
admin.site.register(m.Tag, TagAdmin)
