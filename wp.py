#!/usr/bin/python3

from termcolor import colored
from acf.acf import acfFunc
from init import init
from utils.aiwm import aiwmFunc
from utils.convert_fonts import convertFontsFunc
from utils.create_project import createProject
from utils.pages import wpPages
from utils.plugins import pluginsFunc
from utils.themes import wpThemesFunc
from wp_files.files import mainMenu

print(colored("1) Init", "green"))
print(colored("2) Files", "blue"))
print(colored("3) Acf", "yellow"))
print(colored("4) Backups", "green"))
print(colored("5) Plugins", "blue"))
print(colored("6) Create Project", "blue"))
print(colored("7) Convert Fonts", "yellow"))
print(colored("8) Themes", "green"))
print(colored("9) Pages", "blue"))
print(colored("10) Exit", "red"))

choice = input("Enter your choice: ")
if choice == '1':
    init()
elif choice == '2':
    mainMenu()
elif choice == '3':
    acfFunc()
elif choice == '4':
    aiwmFunc()
elif choice == '5':
    pluginsFunc()
elif choice == '6':
    createProject()
elif choice == '7':
    convertFontsFunc()
elif choice == '8':
    wpThemesFunc()
elif choice == '9':
    wpPages()
else:
    exit()
