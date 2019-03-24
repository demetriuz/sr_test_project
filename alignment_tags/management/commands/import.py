import csv
import logging

from django.core.management.base import LabelCommand
from django.db import transaction

from aligment_tags_domain.importer import Importer

from django.apps.registry import apps

logger = logging.getLogger(__name__)


class Command(LabelCommand):
    help = 'Import data from CSV'

    def handle_label(self, label, **options):
        with open(label, newline='') as csvfile:
            reader = csv.reader(csvfile)

            headers = []
            rows = []

            for idx, row in enumerate(reader):
                if idx == 0:
                    headers = row
                else:
                    rows.append(row)

        service = apps.get_app_config('alignment_tags').get_service()

        with transaction.atomic():
            try:
                Importer(service=service, tag_definition_headers=('FULL_CODE', 'DESCRIPTION')).import_data(headers, rows)
            except Exception as e:
                logger.error('Import error: %s', label)
