from alignment_tags import models as m


def given_definition_level(level_type, value, parent=None):
    return m.DefinitionLevel.objects.create(type=level_type, value=value, parent=parent)


def given_definition_level_type(name, is_internal=False):
    return m.DefinitionLevelType.objects.create(name=name, is_internal=is_internal)


def given_tag(parent_level, code, description=None):
    return m.Tag.objects.create(parent_level=parent_level, code=code, description=description)
