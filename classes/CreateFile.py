import os

from classes.FilesHandle import FilesHandle
from classes.Utils import Utils

script_path = os.path.expanduser('~/Documents/python/wp-python/')

layout_types = (
        {
            'type': 'php',
            'dir_name': 'template-parts',
            'layout_text': 'home',
            'create_file_input_placeholder': 'home',
            'extension': 'php',
            'layout_path': f'{script_path}layouts/php-layout.php',
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
            },
        {
            'type': 'phpp',
            'dir_name': '',
            'layout_text': 'phpPageLayout',
            'create_file_input_placeholder': 'page-servizi',
            'extension': 'php',
            'layout_path': f'{script_path}layouts/php-page.php',
            'create_dir': False
            },
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
            'type': 'ts',
            'dir_name': 'src/vue/interfaces',
            'layout_text': 'IDefault',
            'create_file_input_placeholder': 'IProduct',
            'extension': 'ts',
            'layout_path': f'{script_path}layouts/interface.ts',
            'create_dir': False
            },
        {
            'type': 'vue_view',
            'dir_name': 'src/vue/views',
            'layout_text': 'vue',
            'create_file_input_placeholder': 'myComponent',
            'extension': 'vue',
            'layout_path': f'{script_path}layouts/vue-component.vue',
            'create_dir': False
            },
        {
            'type': 'vue',
            'dir_name': 'src/vue/components',
            'layout_text': 'vue',
            'create_file_input_placeholder': 'myComponent',
            'extension': 'vue',
            'layout_path': f'{script_path}layouts/vue-component.vue',
            'create_dir': True
            },
        {
                'type': 'hook',
                'dir_name': 'src/vue/hooks',
                'layout_text': 'useDefault',
                'create_file_input_placeholder': 'useDefault',
                'extension': 'ts',
                'layout_path': f'{script_path}layouts/default-hook.ts',
                'create_dir': False
                },
        {
                'type': 'pinia',
                'dir_name': 'src/vue/pinia',
                'layout_text': 'useDefault',
                'create_file_input_placeholder': 'default',
                'extension': 'ts',
                'layout_path': f'{script_path}layouts/default-pinia.ts',
                'create_dir': False
                },
        )

getLayoutType = lambda type: next((layout for layout in layout_types if layout['type'] == type))

class CreateFile:
    def __init__(self, type: str):
        self.dir_name = getLayoutType(type)['dir_name']
        self.type = getLayoutType(type)['type']
        if (self.type != 'phpp'):
            self.checkDirPath()
        self.layout_path = getLayoutType(type)['layout_path']
        self.selected_dir = self.createOrChooseDirectory()
        self.layout_text = getLayoutType(type)['layout_text']
        self.create_file_input_placeholder = getLayoutType(type)['create_file_input_placeholder']
        self.extension = getLayoutType(type)['extension']
        self.file_name = ''

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
        if getLayoutType(self.type) == 'phpp':
            files_handle = FilesHandle(self.dir_name)
            files_handle.listFilesWithPrefix(["page-", "single-"])
        self.file_name = input(f"Enter file name like {self.create_file_input_placeholder}: ")
        if self.file_name == '':
            print("File name is required")
            exit()
        if self.type == 'pinia':
            self.file_name = f"{self.file_name}-store"
        if self.selected_dir:
            file_path = f"{self.dir_name}/{self.selected_dir}/{self.file_name}.{self.extension}"
        elif self.type == 'phpp':
            file_path = f"{self.file_name}.{self.extension}"
        else:
            file_path = f"{self.dir_name}/{self.file_name}.{self.extension}"
        with open(self.layout_path, "r") as f:
            layout = f.read()
            if os.path.exists(file_path):
                print("File exists")
                exit()
            else:
                with open(file_path, "w") as f:
                    f.write(layout)
                    print("File created: "+file_path)

        if self.type == 'vue_view' or self.type == 'vue':
            self.file_name = Utils().camelToKebabCase(self.file_name)

        if getLayoutType(self.type)['type'] == 'pinia':
            self.file_name = self.file_name.split('-')[0].lower()
            os.system(f"sed -i -e 's/default/{self.file_name}/g' '{file_path}' ")
            self.file_name = self.file_name.split('-')[0]
            self.file_name = f"use{self.file_name.capitalize()}"
            os.system(f"sed -i -e 's/{self.layout_text}/{self.file_name}/g' '{file_path}' ")
        elif getLayoutType(self.type)['type'] != 'phpp':
            os.system(f"sed -i -e 's/{self.layout_text}/{self.file_name}/g' '{file_path}' ")
        
        if self.type == 'php':
            self.includeInPage()

        os.system(f"bat {file_path}")

    def includeInPage(self):
        if self.type == 'php':
            selected_file = FilesHandle('.').chooseFile()
            print(f"selected_file: {selected_file}")
            self.insertBeforeLastLine(selected_file, f"<?php get_template_part('{self.dir_name}/{self.file_name}');?>\n")


    def insertBeforeLastLine(self, file_path, content):
        # Open the file in read mode
        with open(file_path, 'r') as file:
           lines = file.readlines()
            # Insert a new line before the last line
           lines.insert(-1, content)
           # Open the file again in write mode
        with open(file_path, 'w') as file:
            # Write all the lines back to the file
            file.writelines(lines)
        os.system(f"bat {file_path}")
