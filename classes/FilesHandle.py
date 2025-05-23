import os
from rich import print
from classes.MyTable import MyTable
from libs.select import selectOne
from libs.selectWithFzf import selectWithFzf
from pyfzf.pyfzf import FzfPrompt

class FilesHandle:
    def __init__(self, basepath: str):
        self.basepath = basepath if basepath != '' else '.'

    def listFiles(self):
        files = []
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                files.append([len(files) + 1, entry])

        tb = MyTable()
        tb.show("Files", ["Id","File name"], files)


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

    def listFilesWithPrefix(self, prefix):
        print(f"Listing directories in ================ {self.basepath}")
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                for item in prefix:
                    if entry.startswith(item):
                        print(entry)
        print(f"Listing directories in ================ {self.basepath}")

    def selectWithFzf(self, items):
        fzf = FzfPrompt()
        selected_item = fzf.prompt(items)
        return selected_item[0]

    def chooseFile(self):
        choosed_files = []
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                choosed_files.append(entry)
        if len(choosed_files) == 0:
            exit("[red]No files found")
        else:
            return selectOne(choosed_files)

    def appendToFile(self, file_path, text):
        with open(file_path, "a") as f:
            f.write(text)
        os.system(f"bat {file_path}")
