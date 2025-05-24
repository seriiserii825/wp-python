import os


class Backup:
    def __init__(self):
        pass

    def makeBackup(self, path_to_project=''):
        current_dir = os.getcwd()
        os.system("rm -rf node_modules")
        deleteBackup()
        self.listBackup()
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
        self.listBackup()

    def deleteBackup(self):
        self.listBackup()
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
        pass

    def aiwmFunc(self):
        pass

    def menu(self):
        pass
