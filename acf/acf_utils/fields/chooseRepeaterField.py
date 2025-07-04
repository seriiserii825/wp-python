from acf.acf_utils.fields.getRepeteaterFields import getRepeaterFields


def chooseRepeaterField(file_path, group_index):
    repeater_fields = getRepeaterFields(file_path, group_index)
    if len(repeater_fields) == 0:
        print("No repeater fields found")
        return False
    else:
        for i in repeater_fields:
            print(f"{i['index']}) {i['label']}")

        choice = input("Enter your choice: ")
        if choice == "":
            return False
        else:
            return choice
