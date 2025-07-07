import os

from termcolor import colored

from acf.acf_utils.group.getGroups import getGroups
from libs.buffer import addToClipBoardFile
from libs.file import writeToFile


def copyGroup(file_path):
    groups = getGroups(file_path)
    groups.append(
        {"index": colored(0, "red"), "name": "", "label": colored("Exit", "red")}
    )
    print(colored("Select group:", "green"))
    for i in groups:
        print(f"{i['index']}) {i['label']}")
    group_index = input("Enter your choice: ")
    if group_index != "0":
        group_index = int(group_index)
        group = {}
        for i in groups:
            if i["index"] == group_index:
                group = i
                break
        result = f"""
        ${group["name"]} = get_field('{group["name"]}');
        """
        for field in group["fields"]:
            result += f"""
            ${field["name"]} = ${group["name"]}['{field["name"]}'];
            """
            if len(field["sub_fields"]) > 0:
                for sub_field in field["sub_fields"]:
                    result += f"""
                    ${sub_field["name"]} = $item['{sub_field["name"]}'];
                    """
        writeToFile("result.txt", result)
        command = f"sed -i '/^[[:space:]]*$/d' 'result.txt'"
        os.system(command)
        addToClipBoardFile("result.txt")
        os.system("rm result.txt")
