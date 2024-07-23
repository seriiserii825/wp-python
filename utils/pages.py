import os

from simple_term_menu import subprocess
from termcolor import colored

def createOne():
    title = input("Enter the title: ")
    os.system(f"wp post create --post_type=page --post_status=publish --post_title='{title}'")

def createMultiple():
    titles = input("Enter the titles separated by commas: ")
    print(titles)
    titles = titles.split(",")
    for title in titles:
        title = title.strip()
        os.system(f"wp post create --post_type=page --post_status=publish --post_title='{title}'")

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
    listPages()
    def menu():
        print(colored("1) List pages", "green"))
        print(colored("1.1) Ignore content", "blue"))
        print(colored("2) Create One", "green"))
        print(colored("3) Create Multiple", "green"))
        print(colored("4) Delete One", "red"))
        print(colored("5) Delete Multiple", "red"))
        print(colored("6) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1":
            listPages()
            menu()
        if choice == "1.1":
            ignore()
            menu()
        if choice == "2":
            createOne()
            listPages()
            menu()
        if choice == "3":
            createMultiple()
            listPages()
            menu()
        elif choice == "4":
            deleteOne()
            listPages()
            menu()
        elif choice == "5":
            deleteMultiple()
            listPages()
            menu()
        else:
            exit(colored("Goodbye!", "red"))

    menu()

def ignore():
    listPages()
    user = os.getenv('USER')
    path_to_wp_init = "/home/" + str(user) + "/Documents/python/wp-python/utils/info.sh"
    subprocess.run(["bash", path_to_wp_init])

