import os
import subprocess

from classes.FilesHandle import FilesHandle
from classes.MySelenium import MySelenium
from utils.runCommand import runCommand


class Backup:
    def __init__(self):
        self.backup_dir_abs_path= os.path.abspath("../../ai1wm-backups")
        print(f"self.backup_dir_abs_path=: {self.backup_dir_abs_path=}")
        self.driver = None
    def makeBackup(self):
        self.listBackup()
        current_dir = os.getcwd()
        os.system("rm -rf node_modules")
        try:
            subprocess.run("wp ai1wm backup", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
        self.deleteMore3Backups()
        self.listBackup()
        os.chdir(current_dir)
        self.lastBackupToDownloads()
    def deleteMore3Backups(self):
        os.chdir(self.backup_dir_abs_path)
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
        ms = MySelenium()
        ms.makeBackupInChrome()
    def listBackup(self):
        os.system("wp ai1wm list-backups")
    def restoreBackup(self):
        self.listBackup()
        fh = FilesHandle(self.backup_dir_abs_path)
        selected_backup = fh.chooseFile(self.backup_dir_abs_path, '.wpress')
        os.system(f"wp ai1wm restore {selected_backup}")
    def restoreBackupInChrome(self):
        ms = MySelenium()
        ms.restoreBackupInChrome()
    def restoreFromDownloads(self):
        self.listBackup()
        downloads_dir = os.path.expanduser("~/Downloads")
        fh = FilesHandle(self.backup_dir_abs_path)
        fh.listFiles(downloads_dir)
        selected_backup = fh.chooseFile(downloads_dir, '.wpress')
        print(f"selected_backup: {selected_backup}")
        os.system(f'cp ~/Downloads/{selected_backup} "{self.backup_dir_abs_path}"')
        self.listBackup()
        os.system(f"wp ai1wm restore {selected_backup}")
    def deleteBackupInChrome(self):
        ms = MySelenium()
        ms.deleteBackupInChrome()
    def getLastBackupPath(self):
        os.chdir(self.backup_dir_abs_path)
        backup_files = os.listdir()
        backup_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
        if len(backup_files) == 0:
            print("[red]No backups found!")
        else:
            return backup_files[0]
    def lastBackupToDownloads(self):
        last_backup = self.getLastBackupPath()
        if last_backup:
            backup_path = f"{self.backup_dir_abs_path}/{last_backup}"
            destination = os.path.expanduser("~/Downloads")
            runCommand(["cp", backup_path, destination])
            print(f"[green]Last backup copied to ~/Downloads/{last_backup}")
        else:
            print("[red]No backups found to copy.")
    def lastBackupToMnt(self, mnt_path):
        last_backup = self.getLastBackupPath()
        if last_backup:
            backup_path = f"{self.backup_dir_abs_path}/{last_backup}"
            runCommand(["cp", backup_path, mnt_path])
        else:
            print("[red]No backups found to copy.")
    def createAndCopyToMnt(self):
        directory_exists = os.path.isdir('/mnt/Projects')
        if directory_exists:
            path_to_dir = '/mnt/Projects'
            fh = FilesHandle(path_to_dir)
            selected_dir = fh.createOrChooseDirectory(path_to_dir)
            path_to_selected_dir = path_to_dir + "/" + selected_dir
            fh.listDir(path_to_selected_dir)
            selected_project = fh.createOrChooseDirectory(path_to_selected_dir)
            path_to_selected_dir = path_to_selected_dir + "/" + selected_project
            fh.showOrderFilesByCTime(path_to_selected_dir)
            self.makeBackup()
            self.lastBackupToMnt(path_to_selected_dir)
            fh.showOrderFilesByCTime(path_to_selected_dir)
            exit("[green]Backup created and copied to /mnt/Projects/{selected_project}")
        else:
            exit("[red]Directory /mnt/Projects not exists!")
