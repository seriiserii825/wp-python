from typing import List, Optional, Dict, Any


class Field:
    def __init__(self, data: Dict[str, Any], parent: Optional[str] = None):
        self.key = data.get("key")
        self.label = data.get("label")
        self.name = data.get("name")
        self.type = data.get("type")
        self.sub_fields = data.get("sub_fields", [])
        self.parent = parent

    def parse_fields(self, fields: List[Dict[str, Any]],
                     parent: Optional[str] = None) -> List['Field']:
        from classes.Acf.TextField import TextField
        from classes.Acf.ImageField import ImageField
        from classes.Acf.WysiwygField import WysiwygField
        from classes.Acf.GroupField import GroupField
        from classes.Acf.RepeaterField import RepeaterField
        from classes.Acf.FileField import FileField
        from classes.Acf.GalleryField import GalleryField
        from classes.Acf.TabField import TabField
        from classes.Acf.TextareaField import TextareaField

        FIELD_TYPE_MAP = {
            "text": TextField,
            "textarea": TextareaField,
            "image": ImageField,
            "gallery": GalleryField,
            "file": FileField,
            "wysiwyg": WysiwygField,
            "tab": TabField,
            "group": GroupField,
            "repeater": RepeaterField,
        }

        field_objects = []
        for field in fields:
            field_type = field.get("type")
            cls = FIELD_TYPE_MAP.get(field_type, Field)
            field_objects.append(cls(field, parent))
        return field_objects

    @staticmethod
    def get_field_types() -> List[str]:
        return [
            "text",
            "textarea",
            "image",
            "gallery",
            "file",
            "wysiwyg",
            "tab",
            "group",
            "repeater",
        ]

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.type})>"
