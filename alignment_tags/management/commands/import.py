import csv

from django.core.management.base import LabelCommand
from django.apps.registry import apps

from aligment_tags_domain.iservice import IAlignmentTagsService
from aligment_tags_domain import models as m, errors


class Command(LabelCommand):
    help = 'Import data from CSV'

    def handle_label(self, label, **options):
        service = apps.get_app_config('alignment_tags').get_service()  # type: IAlignmentTagsService

        with open(label, newline='') as csvfile:
            reader = csv.reader(csvfile)

            headers = []
            res = []

            for idx, row in enumerate(reader):
                if idx == 0:
                    headers = row
                else:
                    res.append(row)

        types = []

        if headers[-2] != 'FULL_CODE' and headers[-1] != 'DESCRIPTION':
            raise Exception('Invalid format')

        known_level_types = [level_type.name for level_type in m.LevelTypes]

        for header in headers:
            if header in known_level_types:
                type_to_create = m.LevelType(name=header)
            else:
                type_to_create = m.LevelType(name=header, is_internal=True)

            type_, _ = service.get_or_create_level_type(type_to_create)
            types.append(type_)

        for row in res:
            maybe_parent_level = None
            for idx, cell in enumerate(row):
                    type_ = types[idx]

                    if type_.is_internal:
                        level_to_create = m.Level(type_id=types[idx].id, value=cell)
                        level, _ = service.get_or_create_level(level_to_create)
                    else:
                        level_to_create = m.Level(type_id=types[idx].id,
                                                  value=cell,
                                                  parent_id=maybe_parent_level.id if maybe_parent_level else None)
                        level, _ = service.get_or_create_level(level_to_create)
                        maybe_parent_level = level

            try:
                tag = service.create_tag(m.Tag(parent_level_id=maybe_parent_level.id,
                                         code=row[-2],
                                         description=row[-1]))
                print('Tag added successfully:', tag)

            except errors.DuplicateTagError:
                print('Duplicate Tag:', row)
                continue
