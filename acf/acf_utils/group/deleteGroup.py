import json

from termcolor import colored

from acf.acf_utils.fields.getFields import getFields
from acf.acf_utils.group.getGroups import getGroups
from acf.acf_utils.tabs.getTabs import getTabs


def deleteGroup(file_path):
    fields = getFields(file_path)
    tabs = getTabs(file_path)
    groups = getGroups(file_path)
    print(colored("Select group to delete:", "red"))
    for i in groups:
        print(f"{i['index']}) {i['label']}")
    group_index = input("Enter your choice: ")
    if group_index.isdigit():
        group_index = int(group_index)
        group = fields[0][int(group_index)]
        # print(tabs)
        key = "label"
        val = group["label"]
        tab = next((d for d in tabs if d.get(key) == val), None)
        tab_index = tab["index"]
        with open(file_path, "r") as file:
            data = json.load(file)
            del data[0]["fields"][group_index]
            del data[0]["fields"][tab_index]
            newData = json.dumps(data, indent=4)

        with open(file_path, "w") as file:
            # write
            file.write(newData)
