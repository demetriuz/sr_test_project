from typing import List

from django.db import IntegrityError

from aligment_tags_domain import dtos
from aligment_tags_domain.idao import IAlignmentTagsDAO
from aligment_tags_domain import models as domain_models
from aligment_tags_domain import errors
from .utils import map_errors
from . import models as m


class AlignmentTagsDAO(IAlignmentTagsDAO):
    def get_levels(self, parent_id: int) -> List[dtos.LevelItemDTO]:
        attrs_qs = m.Level.objects.filter(parent_id=parent_id, type__is_internal=False).select_related('type')
        tags_qs = m.Tag.objects.filter(parent_level_id=parent_id)

        return [dtos.LevelItemDTO(id=o.id, value=o.value, type=o.type.name, description=None) for o in attrs_qs] + \
               [dtos.LevelItemDTO(id=o.id, value=o.code, type=dtos.TAG_TYPE, description=o.description) for o in tags_qs]

    def get_or_create_level(self, level: domain_models.Level) -> (domain_models.Level, bool):
        level_, is_created = m.Level.objects.get_or_create(
            type_id=level.type_id,
            value=level.value,
            parent_id=level.parent_id
        )
        level.id = level_.id
        return level, is_created

    @map_errors({
        IntegrityError: errors.DuplicateTagError
    })
    def create_tag(self, tag: domain_models.Tag) -> domain_models.Tag:
        tag_ = m.Tag.objects.create(parent_level_id=tag.parent_level_id, code=tag.code, description=tag.description)
        tag.id = tag_.id
        return tag

    def get_or_create_level_type(self, level_type: domain_models.LevelType) -> (domain_models.LevelType, bool):
        level_type_, is_created = m.LevelType.objects.get_or_create(
            name=level_type.name,
            is_internal=level_type.is_internal
        )
        level_type.id = level_type_.id
        return level_type, is_created
