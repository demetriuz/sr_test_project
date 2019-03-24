import attr

TAG_TYPE = 'TAG'


@attr.s
class DefinitionLevelOrTagDTO:
    id = attr.ib()
    value = attr.ib()
    description = attr.ib()
    type = attr.ib()
