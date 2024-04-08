#!/usr/bin/python3

from init import init
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
    print("Backups")
elif choice == '5':
    print("Plugins")
elif choice == '6':
    exit()
