import os

from termcolor import colored

from libs.camelToKebabCase import camelToKebabCase
from libs.listFiles import listFiles
from wp_files.wp_files.checkCssLayout import checkCssLayout
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory


def createScssFile(dir_name_param="", file_name_param=""):
    if not os.path.exists("src/scss"):
        os.makedirs("src/scss")
    if not os.path.exists("src/scss/layouts"):
        os.makedirs("src/scss/layouts")
    if not os.path.exists("src/scss/default.scss"):
        with open("src/scss/default.scss", "w") as f:
            f.write(".home { &__title{} }")
    scss_layout_path = "src/scss/layouts/default.scss"
    checkCssLayout(scss_layout_path)
    path_to_my_scss = "src/scss/my.scss"
    path_to_dir = "src/scss/blocks"
    path_for_my_scss = "blocks/"
    if dir_name_param != "":
        path_for_my_scss = "blocks/" + dir_name_param
        path_to_selected_dir = path_to_dir + "/" + dir_name_param
        if not os.path.exists(path_to_selected_dir):
            os.makedirs(path_to_selected_dir)
    else:
        selected_dir = createOrChooseDirectory(path_to_dir)
        path_for_my_scss = "blocks/" + selected_dir
        path_to_selected_dir = path_to_dir + "/" + selected_dir
    print(f"Selected dir: {path_to_selected_dir}")
    listFiles(path_to_selected_dir)
    if file_name_param != "":
        file_name = file_name_param
        file_name = camelToKebabCase(file_name)
    else:
        file_name = input("Enter file name: ")
        if file_name == "":
            print(colored("File name is required", "red"))
            exit()
    file_path = path_to_selected_dir + "/" + file_name + ".scss"
    with open(scss_layout_path, "r") as f:
        layout = f.read()
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(layout)
                print(colored("File created: " + file_path, "green"))
    os.system(f"sed -i -e 's/home/{file_name}/g' '{file_path}' ")
    # remove empty lines
    os.system(f"sed -i '/^$/d' {file_path}")
    os.system(f"bat {file_path}")
    with open(path_to_my_scss, "a") as f:
        f.write(f'@import "{path_for_my_scss}/{file_name}";\n')
    os.system(f"bat {path_to_my_scss}")
