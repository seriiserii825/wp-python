import glob
import os
import subprocess

from termcolor import colored
from backups.deleteBackup import deleteBackup
from backups.listBackup import listBackup


def makeBackup(path_to_project=''):
    current_dir = os.getcwd()
    deleteBackup()
    listBackup()
    os.system("rm -rf node_modules")
    try:
        subprocess.run("wp ai1wm backup", shell=True, check=True)
        print("Command was successful")
        #print current dir
        print(f"Current dir: {os.getcwd()}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(f"Current dir: {os.getcwd()}")

    print(f"Current dir: {os.getcwd()}")
    list_of_files = glob.glob('*.wpress')
    print(f"list_of_files: {list_of_files}")
    latest_file = max(list_of_files, key=os.path.getctime)
    if not list_of_files:
        backup_files = os.listdir(".")
        for file in backup_files:
            if file.endswith('.wpress'):
                os.system(f"cp {file} ~/Downloads")
                if path_to_project != "":
                    os.system(f"cp {file} {path_to_project}")
    else:
        latest_file = max(list_of_files, key=os.path.getctime)
        os.system(f"cp {latest_file} ~/Downloads")
        if path_to_project != "":
            os.system(f"cp {latest_file} {path_to_project}")
    print(colored(f"Backup file: {latest_file}", "blue"))
    #go to current_dir
    os.chdir(current_dir)
    listBackup()

