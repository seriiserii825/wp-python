import os
from termcolor import colored

from acf.acf_utils.group.duplicateGroup import duplicateGroup
current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
from acf.acf_utils.group.chooseGroup import chooseGroup
from acf.acf_utils.group.editGroup import editGroup
from acf.acf_utils.group.groupMenu import groupMenu
from acf.acf_utils.group.showAll import showAll
from acf.acf_utils.group.addGroup import addGroup
from acf.acf_utils.group.deleteGroup import deleteGroup
from acf.acf_utils.group.copyGroup import copyGroup
from acf.acf_utils.section.newSection import newSection
from acf.acf_utils.wp.wpExport import wpExport
from acf.acf_utils.wp.wpImport import wpImport
from acf.acf_utils.group.showGroups import showGroups
os.chdir(current_dir)

def acfFunc():
    def getFullPath():
        os.chdir("acf")
        json_file = os.popen("fzf").read()
        file_path = f"acf/{json_file}"
        file_path = file_path.replace("\n", "")
        os.chdir("..")
        return file_path

    print(colored("Welcome to ACF CLI", "green"))
    print(colored("1) Create new section", "yellow"))
    print(colored("2) Select section", "yellow"))
    print(colored("3) Import", "blue"))
    print(colored("4) Export", "blue"))
    print(colored("5) Exit", "red"))
    choice = input("Make your choice:")
    if choice == "1":
        newSection()
    elif choice == "3":
        wpImport()
    elif choice == "4":
        wpExport()
    elif choice == "5":
        exit()
    else:
        file_path = getFullPath()
        def mainMenu(file_path):
            showAll(file_path)
            print('----------------------------- Menu -----------------------------')
            print(colored("1) Show All:", "yellow"))
            print(colored("2) Choose Group:", "green"))
            print(colored("3) Add Group:", "green"))
            print(colored("4) Edit Group:", "green"))
            print(colored("5) Delete Group:", "green"))
            print(colored("6) Copy Group:", "green"))
            print(colored("6.1) Duplicate Group:", "green"))
            print(colored("7) Import:", "yellow"))
            print(colored("8) Export:", "yellow"))
            print(colored("9) Exit:", "red"))
            action = input("Enter your choice: ")
            print('----------------------------- Menu -----------------------------')
            if action == "1":
                showAll(file_path)
                mainMenu(file_path)
            elif action == "2":
                group_index = chooseGroup(file_path)
                back = groupMenu(file_path, group_index)
                print(f"Back: {back}")
                if back == False or back == None:
                    mainMenu(file_path)
            elif action == "3":
                addGroup(file_path)
                mainMenu(file_path)
            elif action == "4":
                editGroup(file_path)
                mainMenu(file_path)
            elif action == "5":
                deleteGroup(file_path)
                mainMenu(file_path)
            elif action == "6":
                copyGroup(file_path)
                print(colored("Group copied successfully!", "green"))
                exit()
            elif action == "6.1":
                duplicateGroup(file_path)
                exit()
            elif action == "7":
                wpImport()
                exit()
            elif action == "8":
                wpExport()
                exit()
            elif action == "9":
                exit()
            else:
                exit()
        mainMenu(file_path)
