import os

from classes.FilesHandle import FilesHandle

script_path = os.path.expanduser('~/Documents/python/wp-python/')

layout_types = (
        {
            'type': 'js',
            'dir_name': 'src/js/modules',
            'layout_text': 'jsLayout',
            'create_file_input_placeholder': 'homeIntro',
            'extension': 'ts',
            'layout_path': f'{script_path}layouts/js_layout.ts',
            'create_dir': True
            },
        {
            'type': 'phpc',
            'dir_name': 'components',
            'layout_text': 'defaultComponent',
            'create_file_input_placeholder': 'myComponent',
            'extension': 'php',
            'layout_path': f'{script_path}layouts/php-component.php',
            'create_dir': False
            }
        )

getLayoutType = lambda type: next((layout for layout in layout_types if layout['type'] == type))

class CreateFile:
    def __init__(self, type: str):
        self.dir_name = getLayoutType(type)['dir_name']
        self.checkDirPath()
        self.type = getLayoutType(type)['type']
        self.layout_path = getLayoutType(type)['layout_path']
        self.selected_dir = self.createOrChooseDirectory()
        self.layout_text = getLayoutType(type)['layout_text']
        self.create_file_input_placeholder = getLayoutType(type)['create_file_input_placeholder']
        self.extension = getLayoutType(type)['extension']

    def checkDirPath(self):
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

    def listFiles(self):
        files_handle = FilesHandle(self.dir_name)
        files_handle.listFiles()

    def createOrChooseDirectory(self):
        if getLayoutType(self.type)['create_dir']:
            files_handle = FilesHandle(self.dir_name)
            selected_dir = files_handle.createOrChooseDirectory()
            return selected_dir
        else:
            return None

    def createFile(self):
        file_name = input(f"Enter file name like {self.create_file_input_placeholder}: ")
        if file_name == '':
            print("File name is required")
            exit()
        if self.selected_dir:
            file_path = f"{self.dir_name}/{self.selected_dir}/{file_name}.{self.extension}"
        else:
            file_path = f"{self.dir_name}/{file_name}.{self.extension}"
        with open(self.layout_path, "r") as f:
            layout = f.read()
            if os.path.exists(file_path):
                print("File exists")
                exit()
            else:
                with open(file_path, "w") as f:
                    f.write(layout)
                    print("File created: "+file_path)
        os.system(f"sed -i -e 's/{self.layout_text}/{file_name}/g' '{file_path}' ")
        os.system(f"bat {file_path}")
