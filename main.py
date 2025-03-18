#!/usr/bin/python3

from simple_term_menu import TerminalMenu
from acf.acf import acfFunc
from init import init, resetSettings
from menu.contactForms import contactForms
from utils.aiwm import aiwmFunc
from utils.pages import wpPages
from utils.plugins import pluginsFunc
from utils.themes import wpThemesFunc
from utils.wp_images import wpImages
from wp_files.files import mainMenu

menu_items = ["Init", "Reset", "Files", "Acf", "Backups", "Plugins", "Themes", "Pages", "Posts", "Images", "Contact form", "Exit"]

terminal_menu = TerminalMenu(menu_items)
menu_entry_index = terminal_menu.show()

if menu_entry_index == 0:
    init()
if menu_entry_index == 1:
    resetSettings()
elif menu_entry_index == 2:
    mainMenu()
elif menu_entry_index == 3:
    acfFunc()
elif menu_entry_index == 4:
    aiwmFunc()
elif menu_entry_index == 5:
    pluginsFunc()
elif menu_entry_index == 6:
    wpThemesFunc()
elif menu_entry_index == 7:
    wpPages()
elif menu_entry_index == 8:
    wpPages(post_type=True)
elif menu_entry_index == 9:
    wpImages()
elif menu_entry_index == 10:
    contactForms()
elif menu_entry_index == 11:
    exit()
