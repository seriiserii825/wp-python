import os

from classes.FilesHandle import FilesHandle

script_path = os.path.expanduser('~/Documents/python/wp-python/')

class CreateFile:
    def __init__(self, dir_name: str, type: str):
        self.dir_name = dir_name
        self.checkDirPath()
        self.type = type
        self.layout_path = ''
        self.setLayoutPath()
        self.selected_dir = self.createOrChooseDirectory()

    def checkDirPath(self):
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

    def listFiles(self):
        files_handle = FilesHandle(self.dir_name)
        files_handle.listFiles()

    def setLayoutPath(self):
        if self.type == 'js':
            self.layout_path = f'{script_path}layouts/js_layout.ts'

    def createOrChooseDirectory(self):
        files_handle = FilesHandle(self.dir_name)
        selected_dir = files_handle.createOrChooseDirectory()
        return selected_dir

    def createFile(self, create_file_input_placeholder: str, layout_text: str):
        file_name = input(f"Enter file name like {create_file_input_placeholder}: ")
        if file_name == '':
            print("File name is required")
            exit()
        file_path = f"{self.dir_name}/{self.selected_dir}/{file_name}.{self.type}"
        with open(self.layout_path, "r") as f:
            layout = f.read()
            if os.path.exists(file_path):
                print("File exists")
                exit()
            else:
                with open(file_path, "w") as f:
                    f.write(layout)
                    print("File created: "+file_path)
        os.system(f"sed -i -e 's/{layout_text}/{file_name}/g' '{file_path}' ")
        os.system(f"bat {file_path}")
