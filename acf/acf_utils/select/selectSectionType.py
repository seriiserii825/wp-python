from termcolor import colored


def selectSectionType(types, type="page"):
    print(type, "type")
    if type == "page":
        for i in types:
            # show index
            print(f"{types.index(i)}) id: {i['ID']}, title: {i['post_title']}")
        type_index = input("Select item: ")
        if type_index == "":
            print(colored("Item not selected", "red"))
            return
        return types[int(type_index)]['ID']
    else:
        for i in types:
            # show index
            print(f"{types.index(i)}) {i}")
        type_index = input("Select item: ")
        if type_index == "":
            print(colored("Item not selected", "red"))
            return
        return types[int(type_index)]

