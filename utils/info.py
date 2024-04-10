from simple_term_menu import os, subprocess
from termcolor import colored


def infoFunc():
    print(colored("1) Info", "green"))
    print(colored("2) Ignore", "blue"))

    choice = input("Enter your choice: ")
    if choice == '1':
        info()
        exit()
    elif choice == '2':
        ignore()
        exit()
    else:
        exit()

def info():
    os.system('wp post list --post_type=page --orderby=title --order=asc')

def ignore():
    info()
    user = os.getenv('USER')
    path_to_wp_init = "/home/" + str(user) + "/Documents/python/wp-python/utils/info.sh"
    subprocess.run(["bash", path_to_wp_init])
