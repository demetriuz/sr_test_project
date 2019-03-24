from abc import ABCMeta, abstractmethod
from typing import List

from aligment_tags_domain import dtos
from . import models as m


class IAlignmentTagsDAO(metaclass=ABCMeta):
    @abstractmethod
    def get_levels(self, parent: int) -> List[dtos.LevelItemDTO]:
        pass

    @abstractmethod
    def get_or_create_level(self, level: m.Level) -> (bool, m.Level):
        pass

    @abstractmethod
    def create_tag(self, tag: m.Tag) -> m.Tag:
        pass

    @abstractmethod
    def get_or_create_level_type(self, level_type: m.LevelType) -> (bool, m.LevelType):
        pass
