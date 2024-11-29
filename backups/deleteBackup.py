import os

from termcolor import colored
from backups.listBackup import listBackup


def deleteBackup():
    listBackup()
    os.chdir("../../ai1wm-backups")
    backup_files = os.listdir()
    backup_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
    backups_array = []
    for file in backup_files:
        if file.endswith('.wpress'):
            backups_array.append(file)
    if (len(backups_array) == 0):
        print(colored("No backups found!", "red"))
    elif(len(backups_array) >2):
        backup_to_delete = backups_array[2:]
        print(colored(f"Backups to delete: ", "red"))
        for file in backup_to_delete:
            print(file)
        for file in backup_to_delete:
            os.system(f"rm {file}")
    else:
        print(colored("Backups less than 3", "green"))

