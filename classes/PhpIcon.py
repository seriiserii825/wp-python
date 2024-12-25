from classes.CreateFile import CreateFile

class PhpIcon(CreateFile):
    def __init__(self, type: str, selected_dir = None):
        super().__init__(type, selected_dir)

    def createFile(self):
        self.file_name = self.getFileName()
        print(f'self.file_name: {self.file_name}')
        self.setPhpIconPath()
