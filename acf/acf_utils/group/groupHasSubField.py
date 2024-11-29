import json


def groupHasSubField(file_path,  sub_field_name, group_index=0):
    f = open(file_path,)
    data = json.load(f)
    # newData = json.dumps(data, indent=4)
    # print(sub_field_name, "sub_field_name")
    print(group_index, "group_index")
    print(sub_field_name, "sub_field_name")
    for k in data[0]['fields'][group_index]['sub_fields']:
        if k['name'] == sub_field_name:
            return True
        else:
            continue
    return False

