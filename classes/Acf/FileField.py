from classes.Acf.Field import Field


class FileField(Field):
    def __init__(self, data, parent=None):
        super().__init__(data, parent)
        self.return_format = data.get("return_format", "url")
