#!/usr/bin/python3

from init import init
from utils.aiwm import aiwmFunc
from utils.plugins import pluginsFunc
from wp_files.files import mainMenu
from acf.acf import acfFunc

print("1) Init")
print("2) Files")
print("3) Acf")
print("4) Backups")
print("5) Plugins")
print("6) Exit")

choice = input("Enter your choice: ")
if choice == '1':
    init()
elif choice == '2':
    mainMenu()
elif choice == '3':
    acfFunc()
elif choice == '4':
    aiwmFunc()
elif choice == '5':
    pluginsFunc()
elif choice == '6':
    exit()
