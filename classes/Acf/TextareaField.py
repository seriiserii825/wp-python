from classes.Acf.Field import Field


class TextareaField(Field):
    def __init__(self, data, parent=None):
        super().__init__(data, parent)
        self.placeholder = data.get("placeholder", "")
