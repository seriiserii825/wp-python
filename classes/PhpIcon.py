import pyperclip
from classes.CreateFile import CreateFile

class PhpIcon(CreateFile):
    def __init__(self, type: str, selected_dir = None):
        super().__init__(type, selected_dir)

    def createFile(self):
        self.file_name = self.getFileName()
        print(f'self.file_name: {self.file_name}')
        self.setPhpIconPath()

    def setPhpIconPath(self):
        clipboard_content = pyperclip.paste()
        print(f"clipboard_content: {clipboard_content}")
        if not 'svg' in clipboard_content:
            print("[red]No svg content in clipboard")
            exit()
        self.file_path = f"{self.dir_name}/icon-{self.file_name}.{self.extension}"
        with open(self.file_path, "w") as f:
            f.write(clipboard_content)
        include_path = f"<?php get_template_part('{self.dir_name}/icon-{self.file_name}');?>\n"
        pyperclip.copy(include_path)
        print(f"[blue]{include_path}")

