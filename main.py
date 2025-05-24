#!/usr/bin/python3

from acf.acf import acfFunc
from init import init, resetSettings
from menu.contactForms import contactForms
from utils.aiwm import aiwmFunc
from utils.pages import wpPages
from utils.parseArgs import parseArgs
from utils.plugins import pluginsFunc
from utils.taxonomies import taxonomies
from utils.themes import wpThemesFunc
from utils.wp_images import wpImages
from wp_files.files import mainMenu
from pyfzf.pyfzf import FzfPrompt


def menu():
# main manu
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
        "Taxonomies"
    ]

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
    elif menu_entry[0] == "Taxonomies":
        taxonomies()
    else:
        exit("Goodbye!")

if __name__ == "__main__":
    parseArgs("backup", aiwmFunc, menu)

