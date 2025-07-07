from acf_utils.group.getGroups import getGroups
from termcolor import colored


def selectFieldByGroup(file_path, group_index):
    groups = getGroups(file_path)
    group = 0
    for i in groups:
        if i['index'] == group_index:
            group = i
    print(group)        
    fields = groups[group_index]['sub_fields']
    fields.append({'index': colored(0, 'red'),  'name': '','label': colored('Exit', 'red')})
    print(colored("Select field:", "green"))
    for i in fields:
        print(f"{i['index']}) {i['label']}")
    field_index = input("Enter your choice: ")
    if field_index != "0":
        field_index = int(field_index)
        return field_index
    elif field_index == "0":
        return
    elif group_index == "0":
        return
