import json


def getGroupPathById(file_path, group_id):
    full_path = '';
    f = open(file_path,)
    data = json.load(f)
    for i in data:
        for j in i['fields']:
            if j['type'] == "group":
                if j['key'] == group_id:
                    index = i['fields'].index(j)
                    full_path = f"data[0]['fields'][{index}]"
                else:
                    for k in j['sub_fields']:
                        if k['type'] == "group":
                            if k['key'] == group_id:
                                index = j['sub_fields'].index(k)
                                full_path = f"data[0]['fields'][{i['fields'].index(j)}]['sub_fields'][{index}]"
                            else:
                                for l in k['sub_fields']:
                                    if l['type'] == "group":
                                        if l['key'] == group_id:
                                            index = k['sub_fields'].index(l)
                                            full_path = f"data[0]['fields'][{i['fields'].index(j)}]['sub_fields'][{j['sub_fields'].index(k)}]['sub_fields'][{index}]"
                print(f"full_path: {full_path}")
                return full_path

