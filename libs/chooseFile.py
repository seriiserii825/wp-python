import os

from termcolor import colored

from libs.select import selectOne


def chooseFile(basepath):
    choosed_files = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            choosed_files.append(entry)
    if len(choosed_files) == 0:
        exit(colored("No files found", "red"))
    else:
        return selectOne(choosed_files)
