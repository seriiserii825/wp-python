#!/usr/bin/python3
import os
from termcolor import colored
from rich.console import Console

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
    print(colored("Images in Downloads folder:", "blue"))
    return sorted_images

def importImages(images):
    for image in images:
        for image in images:
            if image.endswith(".jpg"):
                os.system(f"jpegoptim --strip-all --all-progressive -ptm 80 ~/Downloads/{image}")
                os.system("wp media import ~/Downloads/" + image + " --title=" + image)
            else:
                os.system("wp media import ~/Downloads/" + image + " --title=" + image)

def uploadAll():
    images = getImages()
    importImages(images)

def selectImages():
    images = selectMultiple(getImages())
    importImages(images)

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

