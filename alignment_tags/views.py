from django.apps.registry import apps
from django.http import JsonResponse
from django.views.generic import View
from django import forms

from aligment_tags_domain.iservice import IAlignmentTagsService


class LevelsGetForm(forms.Form):
    parent = forms.IntegerField(required=False)


class LevelsAndTags(View):
    def get(self, *args, **kwargs):
        form = LevelsGetForm(data=self.request.GET)
        if not form.is_valid():
            return JsonResponse(data={'errors': form.errors}, status=403)

        parent_id = form.cleaned_data['parent']

        service = apps.get_app_config('alignment_tags').service  # type: IAlignmentTagsService
        return JsonResponse([o.__dict__ for o in service.get_definition_levels_and_tags(parent_id)], safe=False)
