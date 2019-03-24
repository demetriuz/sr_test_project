import logging
from typing import List, Tuple

from . import models as m, errors
from .iservice import IAlignmentTagsService


logger = logging.getLogger(__name__)


class Importer:
    def __init__(self, service: IAlignmentTagsService, tag_definition_headers: Tuple[str, str]):
        self.service = service
        self.tag_definition_headers = tag_definition_headers
        if len(tag_definition_headers) != 2:
            raise Exception('tag_definition_headers must be `([str], [str])`')

    def import_data(self, headers: List[str], rows: List[str]):
        types = []
        if headers[0] != m.DefinitionLevelTypes.STANDARD.name:
            logger.error('Invalid format: STANDARD must be first header')
            return

        if headers[-2] != self.tag_definition_headers[0] and headers[-1] != self.tag_definition_headers[1]:
            logger.error(f'Invalid format: {self.tag_definition_headers} must last columns')
            return

        known_level_types = [level_type.name for level_type in m.DefinitionLevelTypes]

        for header in headers:
            if header in known_level_types:
                type_to_create = m.DefinitionLevelType(name=header)
            elif header in self.tag_definition_headers:
                continue
            else:
                type_to_create = m.DefinitionLevelType(name=header, is_internal=True)

            type_, _ = self.service.get_or_create_definition_level_type(type_to_create)
            types.append(type_)

        for row in rows:
            maybe_parent_level = None
            for idx, cell in enumerate(row):
                if headers[idx] in self.tag_definition_headers:
                    continue

                type_ = types[idx]

                if type_.is_internal:
                    level_to_create = m.DefinitionLevel(type_id=types[idx].id, value=cell)
                    level, _ = self.service.get_or_create_definition_level(level_to_create)
                else:
                    level_to_create = m.DefinitionLevel(type_id=types[idx].id,
                                                        value=cell,
                                                        parent_id=maybe_parent_level.id if maybe_parent_level else None)
                    level, _ = self.service.get_or_create_definition_level(level_to_create)
                    maybe_parent_level = level

            try:
                tag = self.service.create_tag(m.Tag(parent_level_id=maybe_parent_level.id,
                                                    code=row[-2],
                                                    description=row[-1].strip()))
                logger.info('Tag added successfully: %s', tag)

            except errors.DuplicateTagError:
                logger.error('Duplicate Tag: %s', row)
                raise
