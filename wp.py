#!/usr/bin/python3

from termcolor import colored
from acf.acf import acfFunc
from init import init, resetSettings
from menu.contactForms import contactForms
from utils.aiwm import aiwmFunc
from utils.pages import wpPages
from utils.plugins import pluginsFunc
from utils.themes import wpThemesFunc
from utils.wp_images import wpImages
from wp_files.files import mainMenu

print(colored("1) Init", "green"))
print(colored("1.1) Reset", "red"))
print(colored("2) Files", "blue"))
print(colored("3) Acf", "yellow"))
print(colored("4) Backups", "green"))
print(colored("5) Plugins", "blue"))
print(colored("6) Themes", "green"))
print(colored("7) Pages", "blue"))
print(colored("7.1) Posts", "blue"))
print(colored("8) Images", "blue"))
print(colored("9) Contact form", "green"))
print(colored("10) Exit", "red"))

choice = input("Enter your choice: ")
if choice == '1':
    init()
if choice == '1.1':
    resetSettings()
elif choice == '2':
    mainMenu()
elif choice == '3':
    acfFunc()
elif choice == '4':
    aiwmFunc()
elif choice == '5':
    pluginsFunc()
elif choice == '6':
    wpThemesFunc()
elif choice == '7':
    wpPages()
elif choice == '7.1':
    wpPages(post_type=True)
elif choice == '8':
    wpImages()
elif choice == '9':
    contactForms()
else:
    exit()
