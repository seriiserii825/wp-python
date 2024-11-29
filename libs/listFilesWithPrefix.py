import os

from termcolor import colored


def listFilesWithPrefix(basepath, prefix):
    print(colored(f"Listing directories in ================ {basepath}", "blue"))
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            for item in prefix:
                if entry.startswith(item):
                    print(colored(entry, "blue"))
    print(colored(f"Listing directories in ================ {basepath}", "blue"))
