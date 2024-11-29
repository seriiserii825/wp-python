from termcolor import colored
from acf.acf_utils.fields.addField import addField
from acf.acf_utils.fields.breadcrumbs import breadcrumbs
from acf.acf_utils.fields.deleteField import deleteField
from acf.acf_utils.fields.deleteSubField import deleteSubField
from acf.acf_utils.fields.editField import editField
from acf.acf_utils.fields.editSubField import editSubField
from acf.acf_utils.fields.getFields import getFields
from acf.acf_utils.group.copyGroup import copyGroup
from acf.acf_utils.group.showAll import showAll
from acf.acf_utils.wp.wpExport import wpExport
from acf.acf_utils.wp.wpImport import wpImport


def repeaterFieldsMenu(file_path, group_index, field_index):
    fields = getFields(file_path)
    group = fields[0][int(group_index)]
    print("Group: ", group)
    print("Field: ", field_index)
    field = group['sub_fields'][int(field_index)]
    breadcrumbs(group['label'], field['label'])
    showAll(file_path, group_index)
    print(colored("1) Show All:", "yellow"))
    print(colored("1.1) Copy Group:", "yellow"))
    print(colored("2) Add Field:", "blue"))
    print(colored("3) Edit Field:", "blue"))
    print(colored("4) Delete Field:", "blue"))
    print(colored("5) Import:", "red"))
    print(colored("6) Export:", "red"))
    print(colored("7) Back", "blue"))
    print(colored("8) Exit", "red"))
    action = input("Enter your choice: ")
    if action == "1":
        showAll(file_path)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "1.1":
        copyGroup(file_path)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "2":
        # print(f"field_index: {field_index}")
        addField(file_path, group_index, field_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "3":
        editSubField(file_path, group_index, field_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "4":
        deleteSubField(file_path, group_index, field_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    elif action == "5":
        wpImport()
        exit()
    elif action == "6":
        wpExport()
        exit()
    elif action == "7":
        return False
    elif action == "8":
        exit()
    else:
        repeaterFieldsMenu(file_path, group_index, field_index)
