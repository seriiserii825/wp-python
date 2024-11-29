import os

from simple_term_menu import subprocess
from termcolor import colored

def createOne(post_type="page"):
    title = input("Enter the title: ")
    command = f"wp post create --post_type={post_type} --post_status=publish --post_title='{title}'"
    os.system(command)

def createMultiple(post_type="page"):
    titles = input("Enter the titles separated by commas: ")
    print(titles)
    titles = titles.split(",")
    for title in titles:
        title = title.strip()
        command = f"wp post create --post_type={post_type} --post_status=publish --post_title='{title}'"
        os.system(command)

def deleteOne(post_type="page"):
    command = f"wp post list --post_type={post_type}"
    os.system(command)
    ids = input("Enter the id of the page you want to delete: ")
    os.system(f"wp post delete {ids} --force")

def deleteMultiple(post_type="page"):
    command = f"wp post list --post_type={post_type}"
    os.system(command)
    ids = input("Enter the ids of the pages you want to delete separated by commas: ")
    ids = ids.split(",")
    for id in ids:
        os.system(f"wp post delete {id} --force")

def listPages(post_type="page"):
    command = f"wp post list --post_type={post_type}"
    os.system(command)

def duplicate(post_type="page"):
    command = f"wp post list --post_type={post_type}"
    os.system(command)
    ids = input("Enter the id of the posts you want to duplicate, separated by comma: ")
    ids = ids.split(",")
    for id in ids:
        command = f"wp post create --from-post={id}"
        os.system(command)


def wpPosts():
    command = "wp post list --field=post_type"
    os.system(command)
    post_type = input("Enter the post type: ")
    if post_type == "":
        print("Post type is required")
        exit()
    listPages(post_type)
    def menu():
        print(colored("1) List pages", "green"))
        print(colored("1.1) Duplicate", "blue"))
        print(colored("2) Create One", "green"))
        print(colored("3) Create Multiple", "green"))
        print(colored("4) Delete One", "red"))
        print(colored("5) Delete Multiple", "red"))
        print(colored("6) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1":
            listPages(post_type)
            menu()
        if choice == "1.1":
            duplicate(post_type)
            menu()
        if choice == "2":
            createOne(post_type)
            listPages(post_type)
            menu()
        if choice == "3":
            createMultiple(post_type)
            listPages(post_type)
            menu()
        elif choice == "4":
            deleteOne(post_type)
            listPages(post_type)
            menu()
        elif choice == "5":
            deleteMultiple(post_type)
            listPages(post_type)
            menu()
        else:
            exit(colored("Goodbye!", "red"))

    menu()

def ignore():
    listPages()
    user = os.getenv('USER')
    path_to_wp_init = "/home/" + str(user) + "/Documents/python/wp-python/utils/info.sh"
    subprocess.run(["bash", path_to_wp_init])

