import json

from acf.acf_utils.fields.getFields import getFields
from acf.acf_utils.group.showGroups import showGroups


def deleteField(file_path, group_index):
    fields = getFields(file_path)
    showGroups(file_path, True)  # show groups with fields
    group_index = int(group_index)
    group = fields[0][int(group_index)]
    sub_fields = group["sub_fields"]

    for i in sub_fields:
        print(f"{sub_fields.index(i)}) {i['label']}")

    field_index = input("Enter your choice: ")

    if field_index == "":
        return

    with open(file_path, "r") as file:
        data = json.load(file)
        del data[0]["fields"][group_index]["sub_fields"][int(field_index)]
        newData = json.dumps(data, indent=4)

    with open(file_path, "w") as file:
        # write
        file.write(newData)
