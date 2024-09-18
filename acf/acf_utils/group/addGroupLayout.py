from termcolor import colored

def addGroupLayout():
    print(colored("Group layout(Leave blank for block): ", "green"))
    print(colored("1) block", "blue"))
    print(colored("2) table", "yellow"))
    print(colored("3) row", "red"))
    new_group_layout = input(colored("Enter group layout:", "green"))
    if new_group_layout == "1":
        new_group_layout = "block"
    elif new_group_layout == "2":
        new_group_layout = "table"
    elif new_group_layout == "3":
        new_group_layout = "row"
    else:
        new_group_layout = "block"
    return new_group_layout
