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
    def get_levels(self, parent_id: Optional[int] = None) -> List[dtos.LevelItemDTO]:
        pass

    @abstractmethod
    def get_or_create_level(self, level: m.Level) -> (m.Level, bool):
        pass

    @abstractmethod
    def get_or_create_level_type(self, level_type: m.LevelType) -> (m.LevelType, bool):
        pass

    @abstractmethod
    def create_tag(self, tag: m.Tag) -> m.Tag:
        pass
