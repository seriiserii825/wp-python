import json
import os
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
        # data = SelectSection.json_to_dict()
        # pprint(f"data: {data}")
        SelectSection.json_to_fields()

    @staticmethod
    def json_to_fields():
        with open(SelectSection.file_path) as f:
            acf_data = json.load(f)

        fields_data = acf_data[0]["fields"]
        for field_data in fields_data:
            field = Field(field_data)
            if field.type == "group" or field.type == "repeater":
                name = field.name
                key = field.key
                label = field.label
                type = field.type
                Print.info(
                    f"Name: {name}, Key: {key}, Label: {label}, Type: {type}")
            else:
                name = field.name
                key = field.key
                label = field.label
                type = field.type
                Print.info(
                    f"Name: {name}, Key: {key}, Label: {label}, Type: {type}")

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
