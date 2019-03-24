# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps.registry import apps
from django.http import JsonResponse
from django.views.generic import View

from aligment_tags_domain.iservice import IAlignmentTagsService


class Levels(View):
    def get(self, *args, **kwargs):
        parent_id = self.request.GET.get('parent')
        service = apps.get_app_config('alignment_tags').service  # type: IAlignmentTagsService
        return JsonResponse([o.__dict__ for o in service.get_levels(parent_id)], safe=False)
