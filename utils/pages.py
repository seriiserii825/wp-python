import os
from termcolor import colored

from libs.select import selectMultiple, selectOne

def createOne():
    title = input("Enter the title: ")
    os.system(f"wp post create --post-type=page --post-status=publish --post_title={title}")

def createMultiple():
    titles = input("Enter the titles separated by commas: ")
    titles = titles.split(",")
    for title in titles:
        os.system(f"wp post create --post-type=page --post-status=publish --post_title={title}")

def deleteOne():
    os.system("wp post list --post_type=page")
    ids = input("Enter the id of the page you want to delete: ")
    os.system(f"wp post delete {ids} --force")

def deleteMultiple():
    os.system("wp post list --post_type=page")
    ids = input("Enter the ids of the pages you want to delete separated by commas: ")
    ids = ids.split(",")
    for id in ids:
        os.system(f"wp post delete {id} --force")

def listPages():
    os.system("wp post list --post_type=page")


def wpPages():
    def menu():
        print(colored("1) Create One", "green"))
        print(colored("2) Create Multiple", "green"))
        print(colored("3) Delete One", "blue"))
        print(colored("4) Delete Multiple", "yellow"))
        print(colored("5) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1.1":
            listPages()
            menu()
        if choice == "1":
            createOne()
            listPages()
            menu()
        if choice == "2":
            createMultiple()
            listPages()
            menu()
        elif choice == "3":
            deleteOne()
            listPages()
            menu()
        elif choice == "4":
            deleteMultiple()
            listPages()
            menu()
        else:
            exit(colored("Goodbye!", "red"))

    menu()

