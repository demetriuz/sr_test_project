import pytest

from alignment_tags.dao import AlignmentTagsDAO
from . import test_utils


@pytest.mark.django_db
class TestDAO:
    def setup(self):
        self.dao = AlignmentTagsDAO()

    def test_get_levels_empty(self):
        assert self.dao.get_levels_and_tags(parent_id=None) == []

    def test_get_levels_success(self):
        level_type = test_utils.given_definition_level_type(name='DUMMY_LEVEL_TYPE', is_internal=False)
        level1_1 = test_utils.given_definition_level(level_type=level_type, value='LEVEL1.1')
        level2_1 = test_utils.given_definition_level(level_type=level_type, value='LEVEL2.1', parent=level1_1)

        levels = self.dao.get_levels_and_tags(parent_id=level1_1.id)

        assert len(levels) == 1
        assert levels[0].__dict__ == {'id': level2_1.id,
                                      'value': level2_1.value,
                                      'type': level_type.name,
                                      'description': None}
