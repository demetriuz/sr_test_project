import attr


@attr.s
class LevelDTO:
    id = attr.ib()
    value = attr.ib()
    description = attr.ib()
    category = attr.ib()
