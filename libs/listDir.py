import os

from termcolor import colored

def listDir(path):
    print(colored(f"Listing directories in ================ {path}", "blue"))
    directories = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
                # print(colored(entry.name, "green"))
    # sort the directories by title
    directories.sort()
    for directory in directories:
        print(colored(directory, "green"))
    print(colored(f"Listing directories in ================ {path}", "blue"))
