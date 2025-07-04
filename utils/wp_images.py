#!/usr/bin/python3
import os

from termcolor import colored

from classes.ImagesClass import ImagesClass

if not os.path.exists("style.css"):
    exit(colored("Please run this script from the root of your theme folder!", "red"))


def wpImages():
    print(colored("1) Upload all", "green"))
    print(colored("2) Select", "blue"))
    print(colored("3) Delete Image", "red"))
    print(colored("4) Exit", "red"))
    image_class = ImagesClass()
    image_class.replaceSpaceWithUnderscore()

    choice = input("Make your choice:")
    if choice == "1":
        image_class.uploadAll()
        wpImages()
    elif choice == "2":
        image_class.selectImages()
        wpImages()
    elif choice == "3":
        image_class.deleteImage()
        wpImages()
    elif choice == "4":
        exit(colored("Goodbye!", "red"))
    else:
        exit(colored("Goodbye!", "red"))
