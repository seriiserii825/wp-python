import os

from termcolor import colored

from libs.buffer import addToClipBoardFile, getFromClipBoard
from libs.file import writeToFile
from libs.getFilePathWithoutExtenstion import getFilePathWithoutExtension
from libs.listFiles import listFiles


def createPhpIcon():
    clipboard = getFromClipBoard()
    path_to_dir = "template-parts/icons"
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)
        print(colored("Directory created", "green"))
    listFiles(path_to_dir)
    file_name = input("Enter file name, "+ colored("like facebook", "red") +" servizi for icon-facebook.php: ")
    if file_name == '':
        print(colored("File name is required", "red"))
        exit()
    else:
        file_path = path_to_dir + "/icon-" + file_name + '.php'
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(clipboard)
                print(colored("File created: "+file_path, "green"))
        os.system(f"bat {file_path}")
        file_path_without_extension = getFilePathWithoutExtension(file_path)
        result = f"""
        <?php echo get_template_part('{file_path_without_extension}'); ?>
        """
        writeToFile('result.txt', result)
        command=f"sed -i '/^[[:space:]]*$/d' 'result.txt'"
        os.system(command)
        addToClipBoardFile('result.txt')
        os.system('rm result.txt')
