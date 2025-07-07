import json


def getRepeaterFields(file_path, group_index):
    repeater_fields = []
    f = open(
        file_path,
    )
    data = json.load(f)
    sub_fields = data[0]["fields"][group_index]["sub_fields"]
    for k in sub_fields:
        if k["type"] == "repeater":
            repeater_field = {
                "name": k["name"],
                "label": k["label"],
                "index": sub_fields.index(k),
            }
            repeater_fields.append(repeater_field)
        else:
            continue
    return repeater_fields
