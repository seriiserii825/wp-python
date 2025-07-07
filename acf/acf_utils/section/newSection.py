import json
import os

from termcolor import colored

from acf.acf_utils.group.getGroupId import getGroupId
from acf.acf_utils.select.selectSectionType import selectSectionType
from acf.acf_utils.wp.getWpPages import getWpPages
from acf.acf_utils.wp.getWpPosts import getWpPosts
from acf.acf_utils.wp.getWpTaxonomies import getWpTaxonomies
from acf.acf_utils.wp.wpImport import wpImport


def newSection():
    section_name = input("Enter section name: ")
    file_name = section_name.replace(" ", "-").lower()+".json"
    file_path = f"acf/{file_name}"
    if os.path.exists(file_path):
        print(colored("Section already exists", "red"))
        return
    print(colored("Select section type", "green"))
    print("1) Page")
    print("2) Custom Post Type")
    print("3) Taxonomy")
    input_type = input(colored("Enter section type: ", "blue"))
    post_types = []
    section_type_slug = ""
    section_type_value = ""
    pages = getWpPages()
    post_types = getWpPosts()
    taxonomies = getWpTaxonomies()
    if input_type == "1":
        section_type_slug = "page"
        pages = getWpPages()
        section_type_value = selectSectionType(pages)
    if input_type == "2":
        section_type_slug = "post_type"
        post_types = getWpPosts()
        section_type_value = selectSectionType(post_types, "post_type")
    if input_type == "3":
        section_type_slug = "taxonomy"
        taxonomies = getWpTaxonomies()
        section_type_value = selectSectionType(taxonomies, "taxonomy")

    group_id = getGroupId()
    os.system(f"touch {file_path}")
    os.system(f"echo '[]' > {file_path}")
    if section_name != "":
        with open(file_path, 'r') as file:
            # read
            data = json.load(file)
            new_data = {}
            new_data['ID'] = False
            new_data['key'] = group_id
            new_data['title'] = section_name
            new_data['fields'] = []
            new_data['location'] = [
                [
                    {
                        "param": section_type_slug,
                        "operator": "==",
                        "value": f"{section_type_value}"
                    }
                ]
            ]
            new_data['menu_order'] = 0
            new_data['position'] = "normal"
            new_data['style'] = "default"
            new_data['label_placement'] = "top"
            new_data['instruction_placement'] = "label"
            new_data['hide_on_screen'] = ""
            new_data['active'] = True
            new_data['description'] = ""
            new_data['show_in_rest'] = 0
            new_data['_valid'] = True
            data.append(new_data)
            

            newData = json.dumps(data, indent=4)
        with open(file_path, 'w') as file:
            # write
            file.write(newData)
        print(colored("Section created successfully", "green"))
        wpImport()

