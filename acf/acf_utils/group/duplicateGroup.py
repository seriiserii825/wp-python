import json
from termcolor import colored
from acf.acf_utils.fields.getFieldId import getFieldId
from acf.acf_utils.fields.getFields import getFields
from acf.acf_utils.group.addGroupLayout import addGroupLayout
from acf.acf_utils.group.getGroupByGroupId import getGroupByGroupId
from acf.acf_utils.group.getGroupId import getGroupId
from acf.acf_utils.group.getGroupPathById import getGroupPathById
from acf.acf_utils.group.getGroups import getGroups
from acf.acf_utils.section.sectionHasGroup import sectionHasGroup
from acf.acf_utils.tabs.getTabs import getTabs
from acf.acf_utils.tabs.newTab import newTab


def duplicateGroup(file_path):
    # duplicate fields
    fields = getFields(file_path)
    groups = getGroups(file_path)
    print(colored("Select group to duplicate:", "green"))
    for i in groups:
        print(f"{i['index']}) {i['label']}")
    group_index = input("Enter your choice: ")
    if group_index.isdigit():
        group_index = int(group_index)
        group = fields[0][int(group_index)]
        new_group_label = input("Enter group label: ")
        if new_group_label == "":
            print(colored("Group Label can't be empty", "red"))
            return
        new_group_name = new_group_label.lower().replace(" ", "_")
        new_group_id = getFieldId()
        if sectionHasGroup(file_path, new_group_name):
            print(colored("Group already exists!!!", "red"))
            return
        with open(file_path, 'r') as file:
            # read
            data = json.load(file)
            new_group = group
            new_group['key'] = new_group_id
            new_group['label'] = new_group_label
            new_group['name'] = new_group_name
            new_group['sub_fields'] = group['sub_fields']
            ## change all group['subfields'] keys
            for i in new_group['sub_fields']:
                i['key'] = getFieldId()
            new_tab = newTab(new_group_label)
            data[0]['fields'].append(new_tab)
            data[0]['fields'].append(new_group)
            newData = json.dumps(data, indent=4)
        with open(file_path, 'w') as file:
            file.write(newData)
            print(colored("Group duplicated successfully!", "green"))
