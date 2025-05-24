import os
import subprocess

from classes.FilesHandle import FilesHandle


class Backup:
    def __init__(self):
        pass

    def makeBackup(self, path_to_project=''):
        current_dir = os.getcwd()
        os.system("rm -rf node_modules")
        try:
            subprocess.run("wp ai1wm backup", shell=True, check=True)
            print("Command was successful")
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
        os.chdir(current_dir)

    def deleteMore3Backups(self):
        os.chdir("../../ai1wm-backups")
        backup_files = os.listdir()
        backup_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
        backups_array = []
        for file in backup_files:
            if file.endswith('.wpress'):
                backups_array.append(file)
        if (len(backups_array) == 0):
            print("[red]No backups found!")
        elif(len(backups_array) >2):
            backup_to_delete = backups_array[2:]
            print(f"[red]Backups to delete: ")
            for file in backup_to_delete:
                print(file)
            for file in backup_to_delete:
                os.system(f"rm {file}")
        else:
            print("[green]Backups less than 3")

    def makeBackupInChrome(self):
        pass

    def listBackup(self):
        os.system("wp ai1wm list-backups")

    def restoreBackup(self):
        pass

    def restoreBackupInChrome(self):
        pass

    def restoreFromDownloads(self):
        pass

    def downloadBackup(self):
        pass

    def deleteBackupInChrome(self):
        pass

    def createAndCopyToMnt(self):
        directory_exists = os.path.isdir('/mnt/Projects')
        if directory_exists:
            path_to_dir = '/mnt/Projects'
            fh = FilesHandle(path_to_dir)
            fh.listDir(path_to_dir)
        #     selected_dir = createOrChooseDirectory(path_to_dir)
        #     path_to_selected_dir = path_to_dir + "/" + selected_dir
        #     listDir(path_to_selected_dir)
        #     selected_project = createOrChooseDirectory(path_to_selected_dir)
        #     path_to_selected_dir = path_to_selected_dir + "/" + selected_project
        #     sorted_files = orderFiles(path_to_selected_dir)
        #     makeBackup(path_to_selected_dir)
        #     print(f"[blue]Backup file copied to {path_to_selected_dir}")
        #     for file in sorted_files:
        #         print(file)
        # else:
        #     exit("[red]Directory /mnt/Projects not exists!")


    def aiwmFunc(self):
        pass

    def menu(self):
        pass
