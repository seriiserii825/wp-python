from classes.Acf.Field import Field


class ImageField(Field):
    def __init__(self, data, parent=None):
        super().__init__(data, parent)
        self.preview_size = data.get("preview_size")
