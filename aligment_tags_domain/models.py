from typing import Optional

import attr
from enum import Enum


class LevelTypes(Enum):
    STANDARD = 'STANDARD'
    GRADE = 'GRADE'
    LEARNING_DOMAIN = 'LEARNING_DOMAIN'


@attr.s
class LevelType:
    name = attr.ib()  # type: str
    is_internal = attr.ib(default=False)  # type: bool
    id = attr.ib(default=None)  # type: Optional[int]


@attr.s
class Level:
    value = attr.ib()  # type: str
    parent_id = attr.ib(default=None)  # type: Optional[int]
    id = attr.ib(default=None)  # type: Optional[int]
    type_id = attr.ib(default=None)  # type: Optional[int]


@attr.s
class Tag:
    code = attr.ib()  # type: str
    description = attr.ib()  # type: description
    parent_level_id = attr.ib(default=None)  # type: Optional[int]
    id = attr.ib(default=None)  # type: Optional[int]
