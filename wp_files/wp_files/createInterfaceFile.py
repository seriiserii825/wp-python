import os

from termcolor import colored

from libs.listFiles import listFiles
from wp_files.wp_files.checkInterfaceLayout import checkInterfaceLayout


def createInterfaceFile():
    js_layout_path = "template-parts/layouts/interface.ts"
    checkInterfaceLayout(js_layout_path)
    path_to_dir = "src/vue/interfaces"
    path_to_selected_dir = path_to_dir
    listFiles(path_to_dir)
    file_name = input("Enter file name like IOption: ")
    if file_name == "":
        print(colored("File name is required", "red"))
        exit()
    file_path = path_to_selected_dir + "/" + file_name + ".ts"
    with open(js_layout_path, "r") as f:
        layout = f.read()
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(layout)
                print(colored("File created: " + file_path, "green"))
    os.system(f"sed -i -e 's/IDefault/{file_name}/g' '{file_path}' ")
    os.system(f"bat {file_path}")
