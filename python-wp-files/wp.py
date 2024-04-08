#!/usr/bin/python3

import os

from termcolor import colored

from wp_files.createHookFile import createHookFile
from wp_files.createInterfaceFile import createInterfaceFile
from wp_files.createJavascriptFile import createJsFile
from wp_files.createPhpAndScss import createPhpAndScss
from wp_files.createPhpComponentFile import createPhpComponentFile
from wp_files.createPhpIcon import createPhpIcon
from wp_files.createPhpPage import createPhpPage
from wp_files.createPiniaFile import createPiniaFile
from wp_files.createRestApiFile import createRestApiFile
from wp_files.createScssFile import createScssFile
from wp_files.createVueFile import createVueFile

if not os.path.exists("front-page.php"):
    exit(colored("Please run this script from the root of your theme folder!", "red"))

def menu():
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
        menu()
    if choice == "phps":
        createPhpAndScss()
        menu()
    if choice == "phpc":
        createPhpComponentFile()
        menu()
    if choice == "phpp":
        createPhpPage()
        menu()
    if choice == "phpi":
        createPhpIcon()
        menu()
    if choice == "js":
        createJsFile()
        menu()
    if choice == "ts":
        createInterfaceFile()
        menu()
    if choice == "vue":
        createVueFile()
        menu()
    if choice == "hook":
        createHookFile()
        menu()
    if choice == "pinia":
        createPiniaFile()
        menu()
    if choice == "rest":
        createRestApiFile()
        menu()
    if choice == "":
        exit(colored("Goodbye!", "red"))
    elif choice == "exit":
        exit(colored("Goodbye!", "red"))
    else:
        menu()

menu()
