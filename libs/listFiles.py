import os
from termcolor import colored


def listFiles(basepath):
    print(colored("Existing files:", "green"))
    print(colored(f"List files in ================= {basepath}", "blue"))
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            print(colored(entry, "green"))

    print(colored(f"List files in ================= {basepath}", "blue"))
