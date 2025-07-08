import json
import os
from classes.Print import Print
import pandas as pd
from pprint import pprint


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
        data = SelectSection.json_to_dict()
        pprint(f"data: {data}")

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
