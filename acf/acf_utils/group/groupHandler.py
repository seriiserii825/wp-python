import json
from termcolor import colored
from acf_utils.fields.getFields import getFields
from acf_utils.group.getGroups import getGroups
from acf_utils.section.sectionHasGroup import sectionHasGroup
from acf_utils.tabs.getTabs import getTabs


def groupHandler(file_path, delete=False):
    fields = getFields(file_path)
    tabs = getTabs(file_path)
    groups = getGroups(file_path)
    print(colored("Select group to edit:", "green"))
    for i in groups:
        print(f"{i['index']}) {i['label']}")
    group_index = input("Enter your choice: ")
    if group_index.isdigit():
        group_index = int(group_index)
        group = fields[0][int(group_index)]
        # print(tabs)
        key = 'label'
        val = group['label']
        tab = next((d for d in tabs if d.get(key) == val), None)
        # print(tab)
        # print(type(tab))
        tab_index = tab['index']
        if delete == False:
            new_group_name = input("Enter group name: ")
            new_group_slug = new_group_name.replace(" ", "_").lower()
            if sectionHasGroup(file_path, new_group_slug):
                print(colored("Group already exists!!!", "red"))
                return
            if new_group_name != "":
                with open(file_path, 'r') as file:
                    # read
                    data = json.load(file)
                    data[0]['fields'][group_index]['label'] = new_group_name
                    data[0]['fields'][group_index]['name'] = new_group_slug
                    data[0]['fields'][tab_index]['label'] = new_group_name
                    newData = json.dumps(data, indent=4)

                with open(file_path, 'w') as file:
                    # write
                    file.write(newData)
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)
                del data[0]['fields'][group_index]
                del data[0]['fields'][tab_index]
                newData = json.dumps(data, indent=4)

            with open(file_path, 'w') as file:
                # write
                file.write(newData)

