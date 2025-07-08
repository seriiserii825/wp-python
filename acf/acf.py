import os

from termcolor import colored

from acf.acf_utils.section.newSection import newSection
from acf.acf_utils.wp.wpExport import wpExport
from acf.acf_utils.wp.wpImport import wpImport
from menu.select_section import select_section

current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

os.chdir(current_dir)


def acfFunc():
    wpExport()

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
        select_section()
