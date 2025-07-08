from typing import List, Optional, Dict, Any

from classes.Acf.GroupField import GroupField
from classes.Acf.ImageField import ImageField
from classes.Acf.RepeaterField import RepeaterField
from classes.Acf.TextField import TextField
from classes.Acf.WysiwygField import WysiwygField


class Field:
    def __init__(self, data: Dict[str, Any], parent: Optional[str] = None):
        self.key = data.get("key")
        self.label = data.get("label")
        self.name = data.get("name")
        self.type = data.get("type")
        self.parent = parent
        self.FIELD_TYPE_MAP = {
            "text": TextField,
            "image": ImageField,
            "wysiwyg": WysiwygField,
            "group": GroupField,
            "repeater": RepeaterField,
        }

    def _parse_fields(self, fields: List[Dict[str, Any]], parent: Optional[str] = None) -> List[Field]:
        field_objects = []
        for field in fields:
            field_type = field.get("type")
            cls = self.FIELD_TYPE_MAP.get(field_type, Field)
            field_objects.append(cls(field, parent))
        return field_objects

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.type})>"
