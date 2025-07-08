from classes.Acf.Field import Field


class GroupField(Field):
    def __init__(self, data, parent=None):
        super().__init__(data, parent)
        self.sub_fields = self._parse_fields(
            data.get("sub_fields", []), parent=self.name)
