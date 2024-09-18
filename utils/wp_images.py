#!/usr/bin/python3
import os
from termcolor import colored

from libs.select import selectMultiple, selectOne

if not os.path.exists("style.css"):
    exit(colored("Please run this script from the root of your theme folder!", "red"))

def getImages():
    images = []
    downloads_dir = os.path.expanduser("~") + "/Downloads"
    files = os.listdir(downloads_dir)
    for item in files:
        if item.endswith(".jpg") or item.endswith(".png") or item.endswith(".svg"):
            images.append(item)
    sorted_images = sorted(images)
    print(colored("Images in Downloads folder:", "green"))
    return sorted_images

def uploadAll():
    images = getImages()
    for image in images:
        os.system("wp media import ~/Downloads/" + image + " --title=" + image)

def selectImages():
    images = selectMultiple(getImages())
    print(type(images))
    print(f'images: {images}')
    for image in images:
        os.system("wp media import ~/Downloads/" + image + " --title=" + image)

def wpImages():
    print(colored("1) Upload all", "green"))
    print(colored("2) Select", "blue"))
    print(colored("3) Exit", "red"))

    choice = input("Make your choice:")
    if choice == "1":
        uploadAll()
        wpImages()
    elif choice == "2":
        selectImages()
        wpImages()
    elif choice == "6":
        exit(colored("Goodbye!", "red"))
    else:
        exit(colored("Goodbye!", "red"))

