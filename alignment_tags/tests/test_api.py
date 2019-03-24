import pytest
from django.urls import reverse
from django.test import Client

from aligment_tags_domain.dtos import TAG_TYPE
from . import test_utils


@pytest.mark.django_db
class TestAPI:
    def setup(self):
        self.client = Client()

    def test_levels_empty(self):
        res = self.client.get(reverse('alignment_tags:levels'))
        assert res.status_code == 200
        assert res.json() == []

    def test_levels(self):
        level_type = test_utils.given_definition_level_type(name='DUMMY_LEVEL_TYPE', is_internal=False)
        level1_1 = test_utils.given_definition_level(level_type=level_type, value='LEVEL1.1')

        res = self.client.get(reverse('alignment_tags:levels'))
        assert res.status_code == 200
        assert res.json() == [{'id': level1_1.id, 'value': level1_1.value, 'description': None, 'type': level_type.name}]

    def test_levels_with_tag(self):
        level_type = test_utils.given_definition_level_type(name='DUMMY_LEVEL_TYPE', is_internal=False)
        level1_1 = test_utils.given_definition_level(level_type=level_type, value='LEVEL1.1')
        tag = test_utils.given_tag(parent_level=level1_1, code='DUMMY_CODE', description="Tag Description")

        res = self.client.get(reverse('alignment_tags:levels')+f'?parent={level1_1.id}')
        assert res.status_code == 200
        assert res.json() == [
            {'id': tag.id, 'value': tag.code, 'description': tag.description, 'type': TAG_TYPE}]

    def test_invalid_parent(self):
        res = self.client.get(reverse('alignment_tags:levels') + '?parent=invalid')
        assert res.status_code == 403

    def test_parent_not_found(self):
        res = self.client.get(reverse('alignment_tags:levels') + '?parent=8237981273')
        assert res.status_code == 200
        assert res.json() == []
