# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AlignmentTagsConfig(AppConfig):
    name = 'alignment_tags'

    def ready(self):
        self.service = self.get_service()

    def get_service(self):
        from .service import AlignmentTagsService
        from .dao import AlignmentTagsDAO
        self.service = AlignmentTagsService(AlignmentTagsDAO())
        return self.service
