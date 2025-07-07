import os

from termcolor import colored

from libs.chooseFileForWp import chooseFileForWp
from libs.insertBeforeLastLine import insertBeforeLastLine
from libs.listFiles import listFiles
from wp_files.wp_files.checkPhpLayout import checkPhpLayout
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory
from wp_files.wp_files.createScssFile import createScssFile


def createPhpAndScss():
    php_layout_path = "template-parts/layouts/default.php"
    checkPhpLayout(php_layout_path)
    path_to_dir = "template-parts"
    selected_dir = createOrChooseDirectory(path_to_dir)
    path_to_selected_dir = path_to_dir + "/" + selected_dir
    listFiles(path_to_selected_dir)
    file_name = input("Enter file name: ")
    file_path = path_to_selected_dir + "/" + file_name + ".php"
    path_for_template_part = path_to_selected_dir + "/" + file_name
    if file_name == "":
        print(colored("File name is required", "red"))
        exit()
    else:
        with open(php_layout_path, "r") as f:
            layout = f.read()
            if os.path.exists(file_path):
                print(colored("File exists", "red"))
                exit()
            else:
                with open(file_path, "w") as f:
                    f.write(layout)
                    print(colored("File created: " + file_path, "green"))
        os.system(f"sed -i -e 's/home/{file_name}/g' '{file_path}' ")
        os.system(f"bat {file_path}")
        parent_file = chooseFileForWp("./")
        insertBeforeLastLine(
            parent_file,
            "<?php echo get_template_part('" + path_for_template_part + "');?>\n",
        )
        os.system(f"bat {parent_file}")
        createScssFile(selected_dir, file_name)
