#!/usr/bin/python3
from classes.Plugin import Plugin
from rich import print

def pluginsFunc():
    def menu():
        print("[green]1. List")
        print("2[green]. Install Base Plugins")
        print("3[green]. Install Plugins")
        print("4[red]. Uninstall")
        print("5[red]. Exit")
        action = input("Choose action: ")
        if action == "1":
            pl = Plugin()
            pl.listInstalledPlugins()
            menu()
        elif action == "2":
            pl = Plugin()
            pl.installBasePlugins()
            menu()
        elif action == "3":
            pl = Plugin()
            pl.installOtherPlugins()
            menu()
        elif action == "4":
            pl = Plugin()
            pl.uninstallPlugins()
            menu()
        elif action == "5":
            exit()
        else:
            print("Wrong action!")

    menu()
