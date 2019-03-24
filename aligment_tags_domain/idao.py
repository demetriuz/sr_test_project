from abc import ABCMeta, abstractmethod
from typing import List, Optional

from . import dtos
from . import models as m


class IAlignmentTagsDAO(metaclass=ABCMeta):
    @abstractmethod
    def get_levels_and_tags(self, parent_id: Optional[int]) -> List[dtos.DefinitionLevelOrTagDTO]:
        pass

    @abstractmethod
    def get_or_create_definition_level(self, level: m.DefinitionLevel) -> (m.DefinitionLevel, bool):
        pass

    @abstractmethod
    def create_tag(self, tag: m.Tag) -> m.Tag:
        pass

    @abstractmethod
    def get_or_create_definition_level_type(self, level_type: m.DefinitionLevelType) -> (m.DefinitionLevelType, bool):
        pass
