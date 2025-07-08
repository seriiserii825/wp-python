from typing import List, Optional, Dict, Any

from acf.acf_utils.group.getGroupId import getGroupId
from classes.InputValidator import InputValidator


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

    @staticmethod
    def create_field(field_type: str):
        new_data, x_coord, y_coord = Field._new_field_dict(field_type)
        section = Field._section_from_json()
        print(f"section: {section}")

    @staticmethod
    def _new_field_dict(field_type: str):
        group_id = getGroupId()
        label = InputValidator.get_string("Enter field label: ")
        name = label.lower().replace(" ", "_")
        new_data = {}
        new_data["key"] = group_id
        new_data["label"] = label
        new_data["name"] = name
        new_data["type"] = field_type
        x_coord = InputValidator.get_int("Enter x coordinate: ")
        y_coord = input("Enter y coordinate: ")
        return (new_data, x_coord, y_coord)

    @staticmethod
    def _section_from_json() -> List['Field']:
        from classes.Acf.SelectSection import SelectSection
        SelectSection.show_all()
        return SelectSection.json_to_fields()

    def save_to_file(self):
        pass
        # json_data = json.dumps(new_data, indent=4)
        # json_data = f"[{json_data}]\n"  # Wrap in a list for ACF compatibility
        # with open(Section.file_path, "w") as file:
        #     # write
        #     file.write(json_data)
