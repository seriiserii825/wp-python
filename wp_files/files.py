import os

from termcolor import colored

current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current dir: ", os.getcwd())
from classes.CreateFile import CreateFile
from wp_files.wp_files.createHookFile import createHookFile
from wp_files.wp_files.createInterfaceFile import createInterfaceFile
from wp_files.wp_files.createJavascriptFile import createJsFile
from wp_files.wp_files.createPhpAndScss import createPhpAndScss
from wp_files.wp_files.createPhpComponentFile import createPhpComponentFile
from wp_files.wp_files.createPhpIcon import createPhpIcon
from wp_files.wp_files.createPhpPage import createPhpPage
from wp_files.wp_files.createPiniaFile import createPiniaFile
from wp_files.wp_files.createScssFile import createScssFile
from wp_files.wp_files.createVueFile import createVueFile
os.chdir(current_dir)


def mainMenu():
    print(colored("============= Menu ================", "green"))
    print(colored("php(php and scss)", "yellow"))
    print(colored("phps(php and scss)", "yellow"))
    print(colored("phpc(php component)", "yellow"))
    print(colored("phpp(php page)", "yellow"))
    print(colored("phpi(php icon)", "yellow"))
    print(colored("scss", "blue"))
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
        php_file = CreateFile("php")
        php_file.createFile()
        mainMenu()
    if choice == "scss":
        createScssFile()
        mainMenu()
    if choice == "phps":
        createPhpAndScss()
        mainMenu()
    if choice == "phpc":
        phpc_file = CreateFile("phpc")
        phpc_file.createFile()
        mainMenu()
    if choice == "phpp":
        create_page = CreateFile("phpp")
        create_page.createFile()
        mainMenu()
    if choice == "phpi":
        createPhpIcon()
        mainMenu()
    if choice == "js":
        js_file = CreateFile("js")
        js_file.createFile()
        mainMenu()
    if choice == "ts":
        interface_file = CreateFile("ts")
        interface_file.createFile()
        mainMenu()
    if choice == "vue_view":
        vue_file = CreateFile("vue_view")
        vue_file.createFile()
        mainMenu()
    if choice == "vue":
        vue_file = CreateFile("vue")
        vue_file.createFile()
        mainMenu()
    if choice == "hook":
        hook_file = CreateFile("hook")
        hook_file.createFile()
        mainMenu()
    if choice == "pinia":
        # createPiniaFile()
        pinia_file = CreateFile("pinia")
        pinia_file.createFile()
        mainMenu()
    if choice == "":
        exit(colored("Goodbye!", "red"))
    elif choice == "exit":
        exit(colored("Goodbye!", "red"))
    else:
        mainMenu()

