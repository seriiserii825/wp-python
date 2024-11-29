import json
from acf.acf_utils.fields.fieldTypes import fieldTypes
from acf.acf_utils.fields.getFields import getFields
from acf.acf_utils.fields.newField import newField

def editField(file_path, group_index):
    fields = getFields(file_path)
    group = fields[0][int(group_index)]
    sub_fields = group['sub_fields']

    for i in sub_fields:
        print(f"{sub_fields.index(i)}) {i['label']}")

    field_index = input("Enter your choice: ")

    if field_index == "":
        return

    field_name = input("Enter field name: ")

    if field_name == "":
        field_name = sub_fields[int(field_index)]['label']
        field_slug = field_name.replace(" ", "_").lower()
    else:
        field_slug = field_name.replace(" ", "_").lower()

    field_type = sub_fields[int(field_index)]['type']
    field_types = fieldTypes()
    for i in field_types:
        print(f"{field_types.index(i)}) {i}")
    field_type_index = input("Enter your choice: ")
    if field_type_index == "":
        field_type_index = field_types.index(field_type)
    field_type = field_types[int(field_type_index)]
    default_width = sub_fields[int(field_index)]['wrapper']['width']
    field_width = input("Enter field width: ")
    if field_width == "":
        field_width = default_width
    field = newField(field_name, field_slug, field_type, field_width)
    with open(file_path, 'r') as file:
        # read
        data = json.load(file)
        data[0]['fields'][group_index]['sub_fields'][int(field_index)] = field
        newData = json.dumps(data, indent=4)
    with open(file_path, 'w') as file:
        file.write(newData)
