import json


def getGroups(file_path):
    groups = []
    f = open(file_path,)
    data = json.load(f)
    for i in data:
        for j in i['fields']:
            if j['type'] == "group":
                fields = []
                for k in j['sub_fields']:
                    if k['type'] == "repeater" and len(k['sub_fields']) > 0:
                        sub_fields = []
                        for l in k['sub_fields']:
                            field = {'name': l['name'], 'label': l['label']}
                            sub_fields.append(field)
                        field = {'name': k['name'], 'label': k['label'], 'sub_fields': sub_fields}
                        fields.append(field)
                    else:
                        field = {'name': k['name'], 'label': k['label'], 'sub_fields': []}
                        fields.append(field)
                        continue
                group = {'name': j['name'], 'label': j['label'], 'index': i['fields'].index(j), 'fields': fields}
                # print(json.dumps(group, indent=4))
                groups.append(group)
    # print(groups)
    return groups
