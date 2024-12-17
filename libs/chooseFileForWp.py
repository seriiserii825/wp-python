import os

from termcolor import colored

from libs.selectWithFzf import selectWithFzf


def chooseFileForWp(basepath):
    choosed_files = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            if entry.startswith("page-") or entry.startswith("single-") or entry.startswith("front-"):
                choosed_files.append(entry)
    if len(choosed_files) == 0:
        exit(colored("No files found", "red"))
    else:
        selected_dir = selectWithFzf(choosed_files)
        return selected_dir
