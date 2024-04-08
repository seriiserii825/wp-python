#!/usr/bin/python3

from termcolor import colored
from acf.acf import acfFunc
from init import init
from utils.aiwm import aiwmFunc
from utils.convert_fonts import convertFontsFunc
from utils.info import infoFunc
from utils.plugins import pluginsFunc
from utils.themes import wpThemesFunc
from wp_files.files import mainMenu

print(colored("1) Init", "green"))
print(colored("2) Files", "blue"))
print(colored("3) Acf", "yellow"))
print(colored("4) Backups", "green"))
print(colored("5) Plugins", "blue"))
print(colored("6) Convert Fonts", "yellow"))
print(colored("7) Themes", "green"))
print(colored("8) Info", "blue"))
print(colored("9) Exit", "red"))

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
    convertFontsFunc()
elif choice == '7':
    wpThemesFunc()
elif choice == '8':
    infoFunc()
else:
    exit()
