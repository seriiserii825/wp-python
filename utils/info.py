from simple_term_menu import os, subprocess


def infoFunc():
    print("1) Info")
    print("2) Ignore")

    choice = input("Enter your choice: ")
    if choice == '1':
        info()
        infoFunc()
    else:
        ignore()
        infoFunc()

def info():
    os.system('wp post list --post_type=page --orderby=title --order=asc')

def ignore():
    info()
    user = os.getenv('USER')
    path_to_wp_init = "/home/" + str(user) + "/Documents/python/wp-python/utils/info.sh"
    subprocess.call(path_to_wp_init, shell=True)
