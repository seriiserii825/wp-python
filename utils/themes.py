#!/usr/bin/python3
import os
from termcolor import colored

from libs.select import selectMultiple, selectOne

def wpThemesFunc():
    def listThemes():
        os.system("wp theme list")

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
            os.system("wp theme activate " + theme)
        else:
            exit(colored("No theme selected", "red"))

    def deactivateTheme():
        theme = selectOne(getThemes())
        if theme:
            os.system("wp theme deactivate " + theme)
        else:
            exit(colored("No theme selected", "red"))

    def deleteTheme():
        themes = selectMultiple(getThemes())
        print(themes)
        if not themes:
            exit(colored("No theme selected", "red"))
        else:
            for index, value in enumerate(themes):
                os.system("wp theme delete " + value)

    def searchTheme():
        os.system("wp theme search " + input("Enter theme name:"))
    def installTheme():
        os.system("wp theme install " + input("Enter theme name:"))

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

