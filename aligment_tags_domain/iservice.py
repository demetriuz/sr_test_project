from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Optional, List

from .idao import IAlignmentTagsDAO
from . import dtos
from . import models as m


class IAlignmentTagsService(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, dao: IAlignmentTagsDAO):
        pass

    @abstractmethod
    def get_definition_levels_and_tags(self, parent_id: Optional[int] = None) -> List[dtos.DefinitionLevelOrTagDTO]:
        pass

    @abstractmethod
    def get_or_create_definition_level(self, level: m.DefinitionLevel) -> (m.DefinitionLevel, bool):
        pass

    @abstractmethod
    def get_or_create_definition_level_type(self, level_type: m.DefinitionLevelType) -> (m.DefinitionLevelType, bool):
        pass

    @abstractmethod
    def create_tag(self, tag: m.Tag) -> m.Tag:
        pass
