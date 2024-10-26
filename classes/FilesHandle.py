import os
from rich import print
from libs.select import selectOne
from libs.selectWithFzf import selectWithFzf

class FilesHandle:
    def __init__(self, basepath: str):
        self.basepath = basepath

    def listFiles(self):
        print("Existing files:")
        print(f"[green]List files in ================= {self.basepath}")
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                print(f"[blue]{entry}")

        print(f"[green]List files in ================= {self.basepath}")

    def listDir(self):
        print(f"[green]Listing directories in ================ {self.basepath}")
        directories = []
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    directories.append(entry.name)
        directories.sort()
        for directory in directories:
            print(f"[blue]{directory}")
        print(f"[green]Listing directories in ================ {self.basepath}")


    def createOrChooseDirectory(self):
        self.listDir()
        select_or_create = selectOne(["Select", "Create"])
        if select_or_create == "Create":
            dir_name = input("Enter directory name:")
            if dir_name == '':
                print("Directory name is required")
                exit()
            else:
                os.makedirs(self.basepath + "/" + dir_name)
                print("Directory created")
                return dir_name
        else:
            selected_dir = self.chooseDir()
            return selected_dir


    def chooseDir(self):
        choosed_dir = []
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    choosed_dir.append(entry.name)
        choosed_dir.sort()
        selected_dir = selectWithFzf(choosed_dir)
        return selected_dir
