import json

from acf.acf_utils.fields.getFields import getFields


def deleteSubField(file_path, group_index, field_index):
    fields = getFields(file_path)
    group = fields[0][int(group_index)]
    group_sub_fields = group["sub_fields"]
    sub_fields = group_sub_fields[int(field_index)]["sub_fields"]
    if len(sub_fields) == 0:
        print("No sub fields found")
        return

    for i in sub_fields:
        print(f"{sub_fields.index(i)}) {i['label']}")
    sub_field_index = input("Enter your choice: ")
    if sub_field_index == "":
        return

    with open(file_path, "r") as file:
        # read
        data = json.load(file)
        del data[0]["fields"][group_index]["sub_fields"][int(field_index)][
            "sub_fields"
        ][int(sub_field_index)]
        newData = json.dumps(data, indent=4)
    with open(file_path, "w") as file:
        file.write(newData)
