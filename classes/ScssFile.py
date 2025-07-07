import os

from classes.CreateFile import CreateFile
from classes.FilesHandle import FilesHandle


class ScssFile(CreateFile):
    def __init__(self, type: str, selected_dir=None):
        super().__init__(type, selected_dir)

    def createFile(self, file_name="", dir_name=""):
        if dir_name == "" and file_name == "":
            self.file_name = self.getFileName()
            self.dir_name = f"src/scss/blocks/{self.selected_dir}"
        else:
            self.dir_name = dir_name
            if not os.path.exists(f"{self.dir_name}"):
                os.makedirs(f"{self.dir_name}")
            self.file_name = file_name
        self.file_path = f"{self.dir_name}/{self.file_name}.{self.extension}"
        print(f"self.file_path: {self.file_path}")
        self.createNewFile(self.file_path)
        self.layoutToFile()
        file_path = self.file_path.replace("src/scss/", "")
        file_path = file_path.replace(".scss", "")
        self.appendToMyScss(file_path)

    def appendToMyScss(self, file_path):
        self.dir_name = self.dir_name.split("/")[2:][0]
        # check inside my.scss if exists @import or @use
        to_use = "@import"

        with open("src/scss/my.scss", "r") as f:
            lines = f.readlines()
            for line in lines:
                # if exists string @use in line
                if "@use" in line:
                    to_use = "@use"
                    break
        if to_use == "@use":
            FilesHandle(self.dir_name).appendToFile(
                "src/scss/my.scss", f'@use "{file_path}";\n'
            )
        else:
            FilesHandle(self.dir_name).appendToFile(
                "src/scss/my.scss", f'@import "{file_path}";\n'
            )
