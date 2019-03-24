# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import View

from .service import AlignmentTagsService


class Levels(View):
    def get(self, *args, **kwargs):
        parent_id = self.request.GET.get('parent')
        res = AlignmentTagsService().get_children(parent_id)
        return JsonResponse([o.__dict__ for o in res], safe=False)
