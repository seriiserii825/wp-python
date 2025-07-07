import json


def sectionHasGroup(file_path, group_name):
    f = open(file_path,)
    data = json.load(f)
    json.dumps(data, indent=4)
    # print(newData)
    for i in data:
        for j in i['fields']:
            if j['type'] == "group":
                if j['name'] == group_name:
                    return True
    return False

