from typing import List

from django.core.management.base import LabelCommand
import csv
from ...settings import ALIGNMENT_TAGS_CATEGORIES_HIERARCHY
from ... import models as m


def get_parent_attr(attrs: List[m.Level]):
    for attr in reversed(attrs):
        if attr.type.is_internal:
            continue
        return attr


class Command(LabelCommand):
    help = 'Import data from CSV'

    def handle_label(self, label, **options):
        with open(label, newline='') as csvfile:
            reader = csv.reader(csvfile)

            headers = []
            res = []

            for idx, row in enumerate(reader):
                if idx == 0:
                    headers = row
                else:
                    res.append(row)

        # add categories
        types = []

        # TODO: check headers
        if headers[-2] != 'FULL_CODE' and headers[-1] != 'DESCRIPTION':
            raise Exception('Invalid format')

        for header in headers:
            if header not in ALIGNMENT_TAGS_CATEGORIES_HIERARCHY:
                type_, _, = m.LevelType.objects.get_or_create(name=header, is_internal=True)
            else:
                type_, _, = m.LevelType.objects.get_or_create(name=header)
            types.append(type_)

        # create attrs
        for row in res:

            prev_attrs = []
            for idx, cell in enumerate(row):

                # TODO: not always get_or_create
                type_ = types[idx]
                if type_.is_internal:
                    attr, _ = m.Level.objects.get_or_create(type=types[idx], value=cell)
                else:
                    attr, _ = m.Level.objects.get_or_create(type=types[idx], value=cell, parent=get_parent_attr(prev_attrs))

                prev_attrs.append(attr)

            m.Tag.objects.create(code=row[-2], description=row[-1], parent_level=get_parent_attr(prev_attrs))
