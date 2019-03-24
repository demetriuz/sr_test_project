from typing import List, Optional

from . import dtos
from . import models as m
from .idao import IAlignmentTagsDAO
from .iservice import IAlignmentTagsService


class AlignmentTagsService(IAlignmentTagsService):
    def __init__(self, dao: IAlignmentTagsDAO):
        self.dao = dao

    def get_definition_levels_and_tags(self, parent_id: Optional[int] = None) -> List[dtos.DefinitionLevelOrTagDTO]:
        return self.dao.get_levels_and_tags(parent_id)

    def get_or_create_definition_level(self, level: m.DefinitionLevel) -> (m.DefinitionLevel, bool):
        return self.dao.get_or_create_definition_level(level)

    def get_or_create_definition_level_type(self, level_type: m.DefinitionLevelType) -> (m.DefinitionLevelType, bool):
        return self.dao.get_or_create_definition_level_type(level_type)

    def create_tag(self, tag: m.Tag) -> m.Tag:
        return self.dao.create_tag(tag)
