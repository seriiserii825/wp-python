from classes.CreateFile import CreateFile


class PhpFile(CreateFile):
    def __init__(self, type: str, selected_dir=None):
        super().__init__(type, selected_dir)

    def createFile(self, file_name=""):
        dir_name = self.getDirNameFromLayoutType()
        self.file_name = self.getFileName(file_name)
        self.file_path = (
            f"{dir_name}/{self.selected_dir}/{self.file_name}.{self.extension}"
        )
        self.createNewFile(self.file_path)
        self.layoutToFile()
        self.includeInPage()
