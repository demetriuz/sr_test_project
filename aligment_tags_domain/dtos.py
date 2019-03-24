import attr

TAG_TYPE = 'TAG'


@attr.s
class LevelItemDTO:
    id = attr.ib()
    value = attr.ib()
    description = attr.ib()
    type = attr.ib()
