#!/usr/bin/python3

from acf.acf import acfFunc
from init import init, resetSettings
from menu.contactForms import contactForms
from utils.aiwm import aiwmFunc
from utils.pages import wpPages
from utils.plugins import pluginsFunc
from utils.themes import wpThemesFunc
from utils.wp_images import wpImages
from wp_files.files import mainMenu
from pyfzf.pyfzf import FzfPrompt

# This script is a menu-driven program that allows the user to perform various WordPress-related tasks.
menu_items = [
    "Acf",
    "Backups",
    "Contact form",
    "Exit",
    "Files",
    "Images",
    "Init",
    "Pages",
    "Plugins",
    "Posts",
    "Reset",
    "Themes",
]

# menu
fzf = FzfPrompt()
menu_entry = fzf.prompt(menu_items)

if menu_entry[0] == "Init":
    init()
if menu_entry[0] == "Reset":
    resetSettings()
elif menu_entry[0] == "Files":
    mainMenu()
elif menu_entry[0] == "Acf":
    acfFunc()
elif menu_entry[0] == "Backups":
    aiwmFunc()
elif menu_entry[0] == "Plugins":
    pluginsFunc()
elif menu_entry[0] == "Themes":
    wpThemesFunc()
elif menu_entry[0] == "Pages":
    wpPages()
elif menu_entry[0] == "Posts":
    wpPages(post_type=True)
elif menu_entry[0] == "Images":
    wpImages()
elif menu_entry[0] == "Contact form":
    contactForms()
else:
    exit("Goodbye!")
