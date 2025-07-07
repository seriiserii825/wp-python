import os

from classes.CreateFile import CreateFile


class PiniaFile(CreateFile):
    def __init__(self, type: str, selected_dir=None):
        super().__init__(type, selected_dir)

    def createFile(self, file_name=""):
        self.file_name = self.getFileName(file_name)
        self.file_path = f"src/vue/pinia/{self.file_name}-store.ts"
        self.createNewFile(self.file_path)
        self.layoutToFile()
        self.piniaFile()

    def piniaFile(self):
        print(f"self.file_name: {self.file_name}")
        command = f"sed -i -e 's/default/{self.file_name}/g' '{self.file_path}' "
        print(f"command: {command}")
        os.system(command)
