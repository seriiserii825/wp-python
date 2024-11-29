from termcolor import colored
from acf.acf_utils.fields.addField import addField
from acf.acf_utils.fields.breadcrumbs import breadcrumbs
from acf.acf_utils.fields.chooseRepeaterField import chooseRepeaterField
from acf.acf_utils.fields.deleteField import deleteField
from acf.acf_utils.fields.editField import editField
from acf.acf_utils.fields.getFields import getFields
from acf.acf_utils.group.copyGroup import copyGroup
from acf.acf_utils.group.repeaterFieldsMenu import repeaterFieldsMenu

from acf.acf_utils.group.showAll import showAll
from acf.acf_utils.wp.wpExport import wpExport
from acf.acf_utils.wp.wpImport import wpImport


def groupMenu(file_path, group_index):
    print('----------------------------- Group Menu -----------------------------')
    fields = getFields(file_path)
    group = fields[0][int(group_index)]
    breadcrumbs(group['label'])
    showAll(file_path, group_index)
    print(colored("1) Show All:", "yellow"))
    print(colored("1.1) Copy Group:", "yellow"))
    print(colored("2) Add Field:", "blue"))
    print(colored("3) Choose Repeater Field:", "green"))
    print(colored("4) Edit Field:", "blue"))
    print(colored("5) Delete Field:", "blue"))
    print(colored("6) Import:", "red"))
    print(colored("7) Export:", "red"))
    print(colored("8) Exit", "red"))
    print(colored("9) Back to Main Menu", "green"))
    action = input("Enter your choice: ")
    if action == "1":
        showAll(file_path)
        groupMenu(file_path, group_index)
    if action == "1.1":
        copyGroup(file_path)
        groupMenu(file_path, group_index)
    if action == "2":
        addField(file_path, group_index)
        groupMenu(file_path, group_index)
    if action == "3":
        field_index = chooseRepeaterField(file_path, group_index)
        if field_index == False or field_index == None:
            groupMenu(file_path, group_index)
        else:
            back = repeaterFieldsMenu(file_path, group_index, field_index)
            if back == False or back == None:
                groupMenu(file_path, group_index)
    if action == "4":
        editField(file_path, group_index)
        groupMenu(file_path, group_index)
    if action == "5":
        deleteField(file_path, group_index)
        groupMenu(file_path, group_index)
    elif action == "6":
        wpImport()
        exit()
    elif action == "7":
        wpExport()
        exit()
    elif action == "8":
        exit()
    elif action == "9":
        return False
    else:
        groupMenu(file_path, group_index)
