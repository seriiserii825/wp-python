import os
from datetime import datetime
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

    def listDir(self, path_to_list=''):
        directories = []
        if path_to_list:
            self.basepath = path_to_list
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    directories.append(entry.name)
        directories.sort()
        tb = MyTable()
        tb.show("View Folders", ["Id", "Directory name"], [[i + 1, dir_name] for i, dir_name in enumerate(directories)])

    def createOrChooseDirectory(self, path_to_dir=''):
        if path_to_dir:
            self.basepath = path_to_dir
        else:
            self.basepath = os.getcwd()
        self.listDir(self.basepath)
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

    def chooseFile(self, path_to_dir='', extension=None):
        self.showOrderFilesByCTime(path_to_dir)
        choosed_files = []
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                if extension:
                    if entry.endswith(extension):
                        choosed_files.append(entry)
                else:
                    choosed_files.append(entry)
        if len(choosed_files) == 0:
            exit("[red]No files found")
        else:
            return selectOne(choosed_files)

    def appendToFile(self, file_path, text):
        with open(file_path, "a") as f:
            f.write(text)
        os.system(f"bat {file_path}")

    def showOrderFilesByCTime(self, dir_path):
        current_path = os.getcwd()
        os.chdir(dir_path)

        files = os.listdir()
        # Collect (filename, ctime) tuples
        file_ctimes = [(f, os.path.getctime(f)) for f in files if os.path.isfile(f)]

        # Sort by ctime in reverse order
        file_ctimes.sort(key=lambda x: x[1], reverse=True)

        os.chdir(current_path)  # Restore original working directory

        tb = MyTable()
        tb_title = "Files sorted by creation time"
        tb_headers = ["Id", "File name", "Created at"]
        tb_rows = []

        for i, (file, ctime) in enumerate(file_ctimes):
            ctime_human = datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
            tb_rows.append([i + 1, file, ctime_human])

        tb.show(tb_title, tb_headers, tb_rows)
