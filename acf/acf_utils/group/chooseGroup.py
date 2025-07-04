from acf.acf_utils.group.getGroups import getGroups


def chooseGroup(file_path):
    groups = getGroups(file_path)
    print("Choose a group:")
    for group in groups:
        index = group["index"]
        print(f"{index}) {group['label']}")
    choice = input("Make your choice:")
    if choice.isdigit():
        return int(choice)
    else:
        chooseGroup(file_path)
