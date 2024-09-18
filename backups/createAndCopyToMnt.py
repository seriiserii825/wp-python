import os

from termcolor import colored

from backups.makeBackup import makeBackup
from libs.listDir import listDir
from libs.orderFiles import orderFiles
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory


def createAndCopyToMnt():
    directory_exists = os.path.isdir('/mnt/Projects')
    if directory_exists:
        path_to_dir = '/mnt/Projects'
        listDir(path_to_dir)
        selected_dir = createOrChooseDirectory(path_to_dir)
        path_to_selected_dir = path_to_dir + "/" + selected_dir
        listDir(path_to_selected_dir)
        selected_project = createOrChooseDirectory(path_to_selected_dir)
        path_to_selected_dir = path_to_selected_dir + "/" + selected_project
        sorted_files = orderFiles(path_to_selected_dir)
        makeBackup(path_to_selected_dir)
        print(colored(f"Backup file copied to {path_to_selected_dir}", "blue"))
        for file in sorted_files:
            print(file)
    else:
        exit(colored("Directory /mnt/Projects not exists!", "red"))

