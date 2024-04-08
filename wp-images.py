#!/usr/bin/python3
import os
from termcolor import colored

from libs.select import selectMultiple, selectOne

if not os.path.exists("front-page.php"):
    exit(colored("Please run this script from the root of your theme folder!", "red"))

def getImages():
    images = []
    downloads_dir = os.path.expanduser("~") + "/Downloads"
    files = os.listdir(downloads_dir)
    for item in files:
        if item.endswith(".jpg"):
            images.append(item)
    return images

def uploadAll():
    images = getImages()
    for image in images:
        os.system("wp media import ~/Downloads/" + image + " --title=" + image)

def uploadOne():
    image = selectOne(getImages())
    if image:
        os.system("wp post list")
        post_id = input("Enter post id:")
        os.system("wp media import ~/Downloads/" + image + " --title=" + image + " --post_id=" + post_id + " --featured_image")
    else:
        exit(colored("No image selected", "red"))

def menu():
    print(colored("1) Upload all", "green"))
    print(colored("2) Upload One", "blue"))
    print(colored("3) Exit", "red"))

    choice = input("Make your choice:")
    if choice == "1":
        uploadAll()
        menu()
    elif choice == "2":
        uploadOne()
        menu()
    elif choice == "6":
        exit(colored("Goodbye!", "red"))
    else:
        exit(colored("Goodbye!", "red"))

menu()

