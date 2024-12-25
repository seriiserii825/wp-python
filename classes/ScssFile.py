import os
from classes.CreateFile import CreateFile

class ScssFile(CreateFile):
    def __init__(self, type: str, selected_dir = None):
        super().__init__(type, selected_dir)

    def createFile(self, file_name = '', dir_name = ''):
        if dir_name == '' and file_name == '':
            self.file_name = self.getFileName()
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
