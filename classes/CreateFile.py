import os
from rich import print

from classes.FilesHandle import FilesHandle

from utils.layout_types import layout_types

getLayoutType = lambda type: next((layout for layout in layout_types if layout['type'] == type))

class CreateFile:
    def __init__(self, type: str, selected_dir = None):
        self.dir_name = getLayoutType(type)['dir_name']
        self.type = getLayoutType(type)['type']
        # if (self.type != 'phpp'):
        #     self.checkDirPath()
        self.layout_path = getLayoutType(type)['layout_path']
        if selected_dir:
            self.selected_dir = selected_dir
            if not os.path.exists(f"{self.dir_name}/{self.selected_dir}"):
                os.makedirs(f"{self.dir_name}/{self.selected_dir}")
        else:
            self.selected_dir = self.createOrChooseDirectory()
            print(f"self.selected_dir: {self.selected_dir}")
        self.layout_text = getLayoutType(type)['layout_text']
        self.create_file_input_placeholder = getLayoutType(type)['create_file_input_placeholder']
        self.extension = getLayoutType(type)['extension']
        self.file_name = ''
        self.directory_name = ''
        self.file_path = ''

    def checkDirPath(self):
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

    def listFiles(self):
        dir_path = f"{self.dir_name}/{self.selected_dir}" if self.selected_dir else self.dir_name
        files_handle = FilesHandle(dir_path)
        files_handle.listFiles()

    def createOrChooseDirectory(self):
        if getLayoutType(self.type)['create_dir']:
            files_handle = FilesHandle(self.dir_name)
            selected_dir = files_handle.createOrChooseDirectory()
            return selected_dir
        else:
            return None

    def getFileName(self, file_name = ''):
        if file_name != '':
            self.file_name = file_name
            return self.file_name
        else:
            self.listFiles()
            self.file_name = input(f"Enter file name like {self.create_file_input_placeholder}: ")
            print(f"self.file_name from getFileName: {self.file_name}")
            if self.file_name == '':
                print("File name is required")
                exit()
            else:
                return self.file_name

    def layoutToFile(self):
        if self.layout_path != '':
            with open(self.layout_path, "r") as f:
                layout = f.read()
            with open(self.file_path, "w") as f:
                if layout:
                    f.write(layout)
                print("File created: "+self.file_path)
            #remove empty lines
            os.system(f"sed -i '/^$/d' {self.file_path}")
            os.system(f"sed -i -e 's/{self.layout_text}/{self.file_name}/g' '{self.file_path}' ")
            os.system(f"bat {self.file_path}")

    def createNewFile(self, file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")
            print("File created: "+file_path)
        else:
            print("[red]File already exists: "+file_path)

    # def createFile(self, file_path = ''):
    #     # if self.type == 'phpp':
    #     #     files_handle = FilesHandle(self.dir_name)
    #     #     files_handle.listFilesWithPrefix(["page-", "single-"])
    #     # if self.type == 'pinia':
    #     #     self.file_name = f"{self.file_name}-store"
    #     # if self.selected_dir:
    #     #     file_path = f"{self.dir_name}/{self.selected_dir}/{self.file_name}.{self.extension}"
    #     # elif self.type == 'phpp':
    #     #     file_path = f"{self.file_name}.{self.extension}"
    #     # elif self.type == 'phpi':
    #     #     clipboard_content = pyperclip.paste()
    #     #     print(f"clipboard_content: {clipboard_content}")
    #     #     if not 'svg' in clipboard_content:
    #     #         print("[red]No svg content in clipboard")
    #     #         exit()
    #     #     file_path = f"{self.dir_name}/icon-{self.file_name}.{self.extension}"
    #     # else:
    #     #     file_path = f"{self.dir_name}/{self.file_name}.{self.extension}"
    #     self.file_name = self.getFileName(file_name)
    #     file_path = f"{self.dir_name}/{self.file_name}.{self.extension}"
    #     self.layoutToFile()


        # if self.type == 'phpi':
        #     clipboard_content = pyperclip.paste()
        #     with open(file_path, "w") as f:
        #         f.write(clipboard_content)
        #     include_path = f"<?php get_template_part('{self.dir_name}/icon-{self.file_name}');?>\n"
        #     pyperclip.copy(include_path)
        #     print(f"[blue]{include_path}")
        #
        # if self.type == 'vue_view' or self.type == 'vue':
        #     self.file_name = Utils().camelToKebabCase(self.file_name)
        #
        # if self.type == 'pinia':
        #     self.file_name = self.file_name.split('-')[0].lower()
        #     os.system(f"sed -i -e 's/default/{self.file_name}/g' '{file_path}' ")
        #     self.file_name = self.file_name.split('-')[0]
        #     self.file_name = f"use{self.file_name.capitalize()}"
        #     os.system(f"sed -i -e 's/{self.layout_text}/{self.file_name}/g' '{file_path}' ")
        # elif self.type != 'phpp':
        #     os.system(f"sed -i -e 's/{self.layout_text}/{self.file_name}/g' '{file_path}' ")
        
        # if self.type == 'php':
        #     self.includeInPage()

        # if self.type == 'scss':
        #     self.dir_name = self.dir_name.split('/')[2:][0]
        #     FilesHandle(self.dir_name).appendToFile("src/scss/my.scss", f'@import "{self.dir_name}/{self.selected_dir}/{self.file_name}";\n')
        #
        # if self.type == 'phpc':
        #     with open('functions.php', "a") as f:
        #         f.write(f"\nrequire get_template_directory() . '/{file_path}';")
        #     os.system(f"bat functions.php")
        # os.system(f"bat {file_path}")

    def appendToMyScss(self):
        self.dir_name = self.dir_name.split('/')[2:][0]
        FilesHandle(self.dir_name).appendToFile("src/scss/my.scss", f'@import "{self.dir_name}/{self.selected_dir}/{self.file_name}";\n')

    def changeClassName(self, file_path):
        os.system(f"sed -i -e 's/{self.layout_text}/{self.file_name}/g' '{file_path}' ")

    def includeInPage(self):
        if self.type == 'php':
            selected_file = FilesHandle('.').chooseFile()
            print(f"selected_file: {selected_file}")
            self.insertBeforeLastLine(selected_file, f"<?php get_template_part('{self.dir_name}/{self.selected_dir}/{self.file_name}');?>\n")


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

    def returnFilename(self):
        return self.file_name

    def returnDirname(self):
        return self.selected_dir
