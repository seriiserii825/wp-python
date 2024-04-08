import json
def getFields(file_path):
    fields = []
    f = open(file_path,)
    data = json.load(f)
    for i in data:
        fields.append(i['fields'])
    return fields
