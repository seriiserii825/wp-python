#!/usr/bin/python3
import os
from termcolor import colored
from libs.select import selectMultiple, selectOne
from classes.WpCli import WpCli

def wpThemesFunc():
    wp_cli = WpCli()
    def listThemes():
        wp_cli.runWp("theme list")

    listThemes()

    def getThemes():
        themes = []
        current_dir = os.getcwd()
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        dirs = next(os.walk(parent_dir))[1]
        for theme in dirs:
            themes.append(theme)
        return themes

# getThemes()

    def activateTheme():
        theme = selectOne(getThemes())
        if theme:
            wp_cli.runWp("theme activate " + theme)
        else:
            exit(colored("No theme selected", "red"))

    def deactivateTheme():
        theme = selectOne(getThemes())
        if theme:
            wp_cli.runWp("theme deactivate " + theme)
        else:
            exit(colored("No theme selected", "red"))

    def deleteTheme():
        themes = selectMultiple(getThemes())
        print(themes)
        if not themes:
            exit(colored("No theme selected", "red"))
        else:
            for index, value in enumerate(themes):
                wp_cli.runWp("theme delete " + value)

    def searchTheme():
        theme_name = input("Enter theme name:")
        if not theme_name:
            exit(colored("No theme name provided", "red"))
        wp_cli.runWp("theme search " + theme_name)

    def installTheme():
        theme_name = input("Enter theme name:")
        if not theme_name:
            exit(colored("No theme name provided", "red"))
        wp_cli.runWp("theme install " + theme_name + " --activate")

    def menu():
        print(colored("1) Search", "green"))
        print(colored("1.1) Install", "green"))
        print(colored("2) List", "blue"))
        print(colored("3) Activate", "yellow"))
        print(colored("4) Deactivate", "red"))
        print(colored("5) Delete", "red"))
        print(colored("6) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1":
            searchTheme()
            menu()
        if choice == "1.1":
            installTheme()
            menu()
        elif choice == "2":
            listThemes()
            menu()
        elif choice == "3":
            activateTheme()
            menu()
        elif choice == "4":
            deactivateTheme()
            menu()
        elif choice == "5":
            deleteTheme()
            menu()
        elif choice == "6":
            exit(colored("Goodbye!", "red"))
        else:
            exit(colored("Goodbye!", "red"))

    menu()

