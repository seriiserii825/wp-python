import json
import os
from typing import Any, List

from acf.acf_utils.group.getGroupId import getGroupId
from acf.acf_utils.section.SectionMenu import SectionMenu
from acf.acf_utils.wp.getWpPages import getWpPages
from classes.InputValidator import InputValidator
from my_types.NTPage import NTPage


class Section:
    section_name: str = ""
    file_name: str = ""
    file_path: str = ""

    @staticmethod
    def add_name():
        name = InputValidator.get_string("Enter section name: ")
        Section.section_name = name
        Section.set_file_name(name)

    @staticmethod
    def set_file_name(section_name: str) -> None:
        Section.file_name = section_name.replace(" ", "-").lower() + ".json"

    @staticmethod
    def set_file_path(file_name: str):
        Section.file_path = f"acf/{file_name}"
        if not os.path.exists("acf"):
            raise FileNotFoundError("The 'acf' directory does not exist.")
        if os.path.exists(Section.file_path):
            raise FileExistsError(
                f"The file '{file_name}' already exists in the 'acf' directory."
            )

    @staticmethod
    def choose_type() -> int:
        columns = ["Index", "Option"]
        rows = [
            ["1", "Page"],
            ["2", "Custom Post Type"],
            ["3", "Taxonomy"],
            ["4", "Exit"],
        ]
        SectionMenu.display("New Section", columns, rows)
        choice = SectionMenu.choose_option()
        return choice

    @staticmethod
    def new_acf_page():
        page = Section.select_page()
        Section.create_file(slug=page.post_name)

    @staticmethod
    def select_page() -> NTPage:
        row_pages: List[dict[str, Any]] = getWpPages()
        pages: List[NTPage] = [
            NTPage(
                ID=row["ID"],
                post_title=row["post_title"],
                post_name=row["post_name"],
                post_date=row["post_date"],
                post_status=row["post_status"],
            )
            for row in row_pages
        ]
        print(f"pages: {pages}")

        columns = ["Index", "ID", "Title"]
        rows = [
            [str(pages.index(i)), f"{i.ID}", i.post_title] for i in pages
        ]

        SectionMenu.display("New Section", columns, rows)
        index = SectionMenu.choose_option()
        return pages[index]

    @staticmethod
    def create_file(slug: str):
        group_id = getGroupId()
        os.system(f"touch {Section.file_path}")
        os.system(f"echo '[]' > {Section.file_path}")
        with open(Section.file_path, "r") as file:
            # read
            data = json.load(file)
            new_data = {}
            new_data["ID"] = False
            new_data["key"] = group_id
            new_data["title"] = Section.section_name
            new_data["fields"] = []
            new_data["location"] = [
                [
                    {
                        "param": "page",
                        "operator": "==",
                        "value": slug,
                    }
                ]
            ]
            new_data["menu_order"] = 0
            new_data["position"] = "normal"
            new_data["style"] = "default"
            new_data["label_placement"] = "top"
            new_data["instruction_placement"] = "label"
            new_data["hide_on_screen"] = ""
            new_data["active"] = True
            new_data["description"] = ""
            new_data["show_in_rest"] = 0
            new_data["_valid"] = True
            data.append(new_data)

            newData = json.dumps(data, indent=4)
        with open(Section.file_path, "w") as file:
            # write
            file.write(newData)

