from typing import Optional
import attr
from attr.validators import optional
from enum import Enum


check_int = attr.validators.instance_of(int)
check_str = attr.validators.instance_of(str)


class DefinitionLevelTypes(Enum):
    STANDARD = 'STANDARD'
    GRADE = 'GRADE'
    LEARNING_DOMAIN = 'LEARNING_DOMAIN'


@attr.s
class DefinitionLevelType:
    name = attr.ib(validator=check_str)  # type: str
    is_internal = attr.ib(default=False)  # type: bool
    id = attr.ib(validator=optional(check_int), default=None)  # type: Optional[int]


@attr.s
class DefinitionLevel:
    """ Item of tag definition hierarchy level:
    [STANDARD|GRADE|LEARNING_DOMAIN] or non-hieararchy attr like END_GRADE
    """
    value = attr.ib(validator=check_str)  # type: str
    parent_id = attr.ib(validator=optional(check_int), default=None)  # type: Optional[int]
    id = attr.ib(default=None)  # type: Optional[int]
    type_id = attr.ib(default=None)  # type: Optional[int]


@attr.s
class Tag:
    parent_level_id = attr.ib(validator=check_int)  # type: int
    code = attr.ib()  # type: str
    description = attr.ib()  # type: description
    id = attr.ib(validator=optional(check_int), default=None)  # type: Optional[int]

    @code.validator
    def check(self, attribute, value):
        if not value:
            raise ValueError('`code` required')
