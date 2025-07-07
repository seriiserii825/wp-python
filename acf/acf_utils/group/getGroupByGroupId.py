import json


def getGroupByGroupId(file_path, group_id):
    group = {}
    f = open(
        file_path,
    )
    data = json.load(f)
    for i in data:
        for j in i["fields"]:
            if j["type"] == "group":
                print(f"j['key']: {j['key']}")
                print(f"group_id: {group_id}")
                if j["key"] == group_id:
                    group = j
                    return group
                else:
                    continue
            else:
                continue
        return group
