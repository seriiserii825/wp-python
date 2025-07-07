import json

from acf.acf_utils.fields.fieldTypes import fieldTypes
from acf.acf_utils.fields.newField import newField


def addField(file_path, group_index, field_index = False):
    # print(f"field_index: {field_index}")
    field_name = input("Enter field name: ")
    field_slug = field_name.replace(" ", "_").lower()
    if field_name != "":
        field_types = fieldTypes()
        for i in field_types:
            print(f"{field_types.index(i)}) {i}")
        field_type_index = input("Enter your choice: ")
        if field_type_index == "":
            field_type_index = "0"
        field_type = field_types[int(field_type_index)]
        field_width = input("Enter field width: ")
        if field_width == "":
            field_width = "100"
        field = newField(field_name, field_slug, field_type, field_width)
        with open(file_path, 'r') as file:
            # read
            data = json.load(file)
            if field_index != False:
                field_index = int(field_index)
                field_index_path  = data[0]['fields'][group_index]['sub_fields'][field_index]
                # print(f"field_index_path: {field_index_path}")
                field_index_path['sub_fields'].append(field)
            else:
                data[0]['fields'][group_index]['sub_fields'].append(field)
            newData = json.dumps(data, indent=4)
        with open(file_path, 'w') as file:
            file.write(newData)
