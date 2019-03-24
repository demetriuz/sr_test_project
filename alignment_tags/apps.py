from django.apps import AppConfig


class AlignmentTagsConfig(AppConfig):
    name = 'alignment_tags'

    def ready(self):
        self.service = self.get_service()

    def get_service(self):
        from aligment_tags_domain.service import AlignmentTagsService
        from .dao import AlignmentTagsDAO
        self.service = AlignmentTagsService(AlignmentTagsDAO())
        return self.service
