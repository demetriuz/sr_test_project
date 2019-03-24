from typing import List, Optional

from . import models as m
from . import dtos


class AlignmentTagsService:
    def get_children(self, parent_id: Optional[int]=None) -> List[dtos.LevelDTO]:

        attrs_qs = m.Level.objects.filter(parent_id=parent_id, type__is_internal=False)
        tags_qs = m.Tag.objects.filter(parent_level_id=parent_id)

        return [dtos.LevelDTO(id=o.id, value=o.value, category=o.type.name, description=None) for o in attrs_qs] + \
               [dtos.LevelDTO(id=o.id, value=o.code, category='TAG', description=o.description) for o in tags_qs]
