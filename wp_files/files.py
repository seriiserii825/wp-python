import os

from termcolor import colored

current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current dir: ", os.getcwd())
from wp_files.wp_files.createHookFile import createHookFile
from wp_files.wp_files.createInterfaceFile import createInterfaceFile
from wp_files.wp_files.createJavascriptFile import createJsFile
from wp_files.wp_files.createPhpAndScss import createPhpAndScss
from wp_files.wp_files.createPhpComponentFile import createPhpComponentFile
from wp_files.wp_files.createPhpIcon import createPhpIcon
from wp_files.wp_files.createPhpPage import createPhpPage
from wp_files.wp_files.createPiniaFile import createPiniaFile
from wp_files.wp_files.createRestApiFile import createRestApiFile
from wp_files.wp_files.createScssFile import createScssFile
from wp_files.wp_files.createVueFile import createVueFile
os.chdir(current_dir)


def mainMenu():
    print(colored("============= Menu ================", "green"))
    print(colored("scss", "blue"))
    print(colored("phps(php and scss)", "yellow"))
    print(colored("phpc(php component)", "yellow"))
    print(colored("phpp(php page)", "yellow"))
    print(colored("phpi(php icon)", "yellow"))
    print(colored("js", "red"))
    print(colored("ts(interface)", "red"))
    print(colored("vue", "green"))
    print(colored("hook", "green"))
    print(colored("pinia", "green"))
    print(colored("rest(rest api)", "blue"))
    print(colored("exit", "red"))
    print(colored("============= Menu ================", "green"))

    choice = input("Make your choice:")
    if choice == "scss":
        createScssFile()
        mainMenu()
    if choice == "phps":
        createPhpAndScss()
        mainMenu()
    if choice == "phpc":
        createPhpComponentFile()
        mainMenu()
    if choice == "phpp":
        createPhpPage()
        mainMenu()
    if choice == "phpi":
        createPhpIcon()
        mainMenu()
    if choice == "js":
        createJsFile()
        mainMenu()
    if choice == "ts":
        createInterfaceFile()
        mainMenu()
    if choice == "vue":
        createVueFile()
        mainMenu()
    if choice == "hook":
        createHookFile()
        mainMenu()
    if choice == "pinia":
        createPiniaFile()
        mainMenu()
    if choice == "rest":
        createRestApiFile()
        mainMenu()
    if choice == "":
        exit(colored("Goodbye!", "red"))
    elif choice == "exit":
        exit(colored("Goodbye!", "red"))
    else:
        mainMenu()

