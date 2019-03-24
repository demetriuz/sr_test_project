from typing import List, Optional

from aligment_tags_domain.idao import IAlignmentTagsDAO
from aligment_tags_domain import dtos
from aligment_tags_domain import models as m
from aligment_tags_domain.iservice import IAlignmentTagsService


class AlignmentTagsService(IAlignmentTagsService):
    def __init__(self, dao: IAlignmentTagsDAO):
        self.dao = dao

    def get_levels(self, parent_id: Optional[int] = None) -> List[dtos.LevelItemDTO]:
        return self.dao.get_levels(parent_id)

    def get_or_create_level(self, level: m.Level) -> (m.Level, bool):
        return self.dao.get_or_create_level(level)

    def get_or_create_level_type(self, level_type: m.LevelType) -> (m.LevelType, bool):
        return self.dao.get_or_create_level_type(level_type)

    def create_tag(self, tag: m.Tag) -> m.Tag:
        return self.dao.create_tag(tag)
