import json
import os
from typing import List
from rich import print

from classes.Acf.Field import Field
from classes.Print import Print


class SelectSection:
    file_path = ""

    @staticmethod
    def init():
        SelectSection.file_path = SelectSection._get_acf_file_path()

    @staticmethod
    def _get_acf_file_path():
        os.chdir("acf")
        json_file = os.popen("fzf").read()
        file_path = f"acf/{json_file}"
        file_path = file_path.replace("\n", "")
        os.chdir("..")
        return file_path

    @staticmethod
    def show_all():
        Print.info(SelectSection.file_path)
        fields: List[Field] = SelectSection.json_to_fields()
        SelectSection.draw_schema(fields)

    @staticmethod
    def json_to_fields() -> List[Field]:
        with open(SelectSection.file_path) as f:
            acf_data = json.load(f)

        fields_data = acf_data[0]["fields"]
        fields_array = []
        for field_data in fields_data:
            field = Field(field_data)
            if field.sub_fields:
                field.sub_fields = field.parse_fields(
                    field.sub_fields, field.key)
            fields_array.append(field)
        return fields_array

    @staticmethod
    def draw_schema(field: List[Field]):
        Print.info("Drawing schema for fields:")
        for index, f in enumerate(field, start=0):
            if f.type == "tab":
                SelectSection.print_field(f=f, color="blue", index=index)
            elif f.type == "group":
                SelectSection.print_field(f=f, color="green", index=index)
            else:
                SelectSection.print_field(f=f, color="yellow", index=index)
            if f.sub_fields:
                for idx, sub_field in enumerate(f.sub_fields, start=0):
                    if sub_field.type == "tab":
                        SelectSection.print_field_with_subfields(
                            f=sub_field, color="blue", index=idx)
                    elif sub_field.type == "group":
                        SelectSection.print_field_with_subfields(
                            f=sub_field, color="green", index=idx)
                    else:
                        SelectSection.print_field_with_subfields(
                            f=sub_field, color="yellow", index=idx)

    @staticmethod
    def print_field(f: Field, color: str, index: int):
        print(f"[{color}]{index}): {f.label} - ({f.type}) - {f.name} - {f.key}")

    @staticmethod
    def print_field_with_subfields(f: Field, color: str, index: int):
        print(f"  [{color}]{index}): {f.label} - ({f.type}) - {f.name} - ({f.key})")

    @staticmethod
    def json_to_dict():
        with open(SelectSection.file_path, "r") as file:
            data = file.read()
            data = json.loads(data)
        Print.info(f"data: {data}")
        SelectSection._display_json_content()
        return data

    @staticmethod
    def _display_json_content():
        os.system(f"bat {SelectSection.file_path}")
