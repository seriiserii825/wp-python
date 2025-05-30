import os

from simple_term_menu import subprocess
from termcolor import colored

from classes.WpCli import WpCli

wp_cli = WpCli()

def createOne(post_type="page"):
    title = input("Enter the title: ")
    command = f"post create --post_type={post_type} --post_status=publish --post_title='{title}'"
    wp_cli.runWp(command)


def createMultiple(post_type="page"):
    titles = input("Enter the titles separated by commas: ")
    print(titles)
    titles = titles.split(",")
    for title in titles:
        title = title.strip()
        command = f"post create --post_type={post_type} --post_status=publish --post_title='{title}'"
        wp_cli.runWp(command)


def deleteOne(post_type="page"):
    command = f"post list --post_type={post_type}"
    wp_cli.runWp(command)
    ids = input("Enter the id of the page you want to delete: ")
    command = f"post delete {ids} --force"
    wp_cli.runWp(command)


def deleteMultiple(post_type="page"):
    print(f'post_type: {post_type}')
    # multiple_or_all = input(
    #     "Do you want to delete multiple posts or all? (m/a): ")
    # if multiple_or_all == "m":
    #     command = f"post list --post_type={post_type}"
    #     wp_cli.runWp(command)
    #     ids = input(
    #         "Enter the ids of the pages you want to delete separated by commas: ")
    #     ids = ids.split(",")
    #     for id in ids:
    #         os.system(f"wp post delete {id} --force")
    # elif multiple_or_all == "a":
    #     command = f"post list --post_type={post_type}"
    #     wp_cli.runWp(command)
    #     all_ids = os.popen(f"post list --post_type={post_type} --field=ID").read().strip().split("\n")
    #     for id in all_ids:
    #         os.system(f"wp post delete {id} --force")
    # else:
    #     print("Invalid option. Please choose 'm' or 'a'.")


def listPages(post_type="page"):
    command = f"post list --post_type={post_type}"
    wp_cli.runWp(command)


def duplicate(post_type="page"):
    command = f"post list --post_type={post_type}"
    wp_cli.runWp(command)
    ids = input(
        "Enter the id of the posts you want to duplicate, separated by comma: ")
    ids = ids.split(",")
    for id in ids:
        command = f"post create --from-post={id}"
        wp_cli.runWp(command)


def wpPages(post_type=False):
    if post_type:
        command = "post-type list --capability_type=post --fields=name,public"
        wp_cli.runWp(command)
        post_type = input("Enter the post type: ")
        if post_type == "":
            print("Post type is required")
            exit()
        else:
            post_type = post_type
    else:
        post_type = "page"

    listPages(post_type)

    def menu(post_type):
        print(colored("1) List pages", "green"))
        print(colored("1.1) Ignore content", "blue"))
        print(colored("1.2) Duplicate", "blue"))
        print(colored("2) Create One", "green"))
        print(colored("3) Create Multiple", "green"))
        print(colored("4) Delete One", "red"))
        print(colored("5) Delete Multiple", "red"))
        print(colored("6) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1":
            listPages(post_type)
            menu(post_type)
        if choice == "1.1":
            ignore()
            menu(post_type)
        if choice == "1.2":
            duplicate(post_type)
            menu(post_type)
        if choice == "2":
            createOne(post_type)
            listPages(post_type)
            menu(post_type)
        if choice == "3":
            createMultiple(post_type)
            listPages(post_type)
            menu(post_type)
        elif choice == "4":
            deleteOne(post_type)
            listPages(post_type)
            menu(post_type)
        elif choice == "5":
            deleteMultiple(post_type)
            listPages(post_type)
            menu(post_type)
        else:
            exit(colored("Goodbye!", "red"))

    menu(post_type)


def ignore():
    listPages()
    user = os.getenv('USER')
    path_to_wp_init = "/home/" + \
        str(user) + "/Documents/python/wp-python/utils/info.sh"
    subprocess.run(["bash", path_to_wp_init])
