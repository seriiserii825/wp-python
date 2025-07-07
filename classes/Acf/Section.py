import os
from classes.InputValidator import InputValidator


class Section:
    @staticmethod
    def add_name() -> str:
        name = InputValidator.get_string("Enter section name: ")
        return name

    @staticmethod
    def get_file_name(section_name: str) -> str:
        file_name = section_name.replace(" ", "-").lower() + ".json"
        return file_name

    @staticmethod
    def get_file_path(file_name: str) -> str:
        file_path = f"acf/{file_name}"
        if not os.path.exists("acf"):
            raise FileNotFoundError("The 'acf' directory does not exist.")
        if os.path.exists(file_path):
            raise FileExistsError(
                f"The file '{file_name}' already exists in the 'acf' directory.")
        return file_path
