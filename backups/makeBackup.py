import glob
import os

from termcolor import colored
from backups.listBackup import listBackup


def makeBackup(path_to_project=''):
    listBackup()
    os.system("wp ai1wm backup")
    list_of_files = glob.glob('../../ai1wm-backups/*.wpress')
    latest_file = max(list_of_files, key=os.path.getctime)
    if not list_of_files:
        backup_files = os.listdir(".")
        for file in backup_files:
            if file.endswith('.wpress'):
                os.system(f"cp {file} ~/Downloads")
                if path_to_project != "":
                    os.system(f"cp {file} {path_to_project}")
        listBackup()
    else:
        latest_file = max(list_of_files, key=os.path.getctime)
        os.system(f"cp {latest_file} ~/Downloads")
        if path_to_project != "":
            os.system(f"cp {latest_file} {path_to_project}")
        listBackup()
    print(colored(f"Backup file: {latest_file}", "blue"))

