import os

from termcolor import colored

from classes.DefaultFile import DefaultFile
from classes.PhpFile import PhpFile
from classes.PhpIcon import PhpIcon
from classes.PhpPage import PhpPage
from classes.ScssFile import ScssFile

current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current dir: ", os.getcwd())
os.chdir(current_dir)


def mainMenu():
    print(colored("============= Menu ================", "green"))
    print(colored("php", "yellow"))
    print(colored("phps(php and scss)", "yellow"))
    print(colored("scss", "blue"))
    print(colored("phpc(php component)", "yellow"))
    print(colored("phpp(php page)", "yellow"))
    print(colored("phpi(php icon)", "yellow"))
    print(colored("js", "red"))
    print(colored("ts(interface)", "red"))
    print(colored("vue_view", "green"))
    print(colored("vue(component)", "green"))
    print(colored("hook", "blue"))
    print(colored("pinia", "blue"))
    print(colored("exit", "red"))
    print(colored("============= Menu ================", "green"))

    choice = input("Make your choice:")
    if choice == "php":
        php_file = PhpFile("php")
        php_file.createFile()
        mainMenu()
    if choice == "scss":
        scss_file = ScssFile("scss")
        scss_file.createFile()
        mainMenu()
    if choice == "phps":
        php_file = PhpFile("php")
        php_file.createFile()
        file_name = php_file.returnFilename()
        dir_name = php_file.returnDirname()
        dir_name = f"src/scss/blocks/{dir_name}"
        scss_file = ScssFile("scss", selected_dir=dir_name)
        scss_file.createFile(file_name, dir_name)
        mainMenu()
    if choice == "phpp":
        php_page = PhpPage("phpp")
        php_page.createFile()
        mainMenu()
    if choice == "phpi":
        php_icon = PhpIcon("phpi")
        php_icon.createFile()
        mainMenu()
    if choice == "js":
        js_file = DefaultFile("js")
        js_file.createFile()
        mainMenu()
    if choice == "ts":
        interface_file = DefaultFile("ts")
        interface_file.createFile()
        mainMenu()
    if choice == "vue_view":
        vue_file = DefaultFile("vue_view")
        vue_file.createFile()
        mainMenu()
    if choice == "vue":
        vue_file = DefaultFile("vue")
        vue_file.createFile()
        mainMenu()
    # if choice == "hook":
    #     hook_file = CreateFile("hook")
    #     hook_file.createFile()
    #     mainMenu()
    # if choice == "pinia":
    #     pinia_file = CreateFile("pinia")
    #     pinia_file.createFile()
    #     mainMenu()
    if choice == "":
        exit(colored("Goodbye!", "red"))
    elif choice == "exit":
        exit(colored("Goodbye!", "red"))
    else:
        mainMenu()

