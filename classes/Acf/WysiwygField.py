from classes.Acf.Field import Field


class WysiwygField(Field):
    def __init__(self, data, parent=None):
        super().__init__(data, parent)
        self.toolbar = data.get("toolbar", "")
