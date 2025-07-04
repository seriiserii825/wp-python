import os

from termcolor import colored

from libs.listFiles import listFiles
from wp_files.wp_files.checkPiniaLayout import checkPiniaLayout


def createPiniaFile():
    layout_path = "template-parts/layouts/default-pinia.ts"
    checkPiniaLayout(layout_path)
    path_to_dir = "src/vue/pinia"
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)
    path_to_selected_dir = path_to_dir
    listFiles(path_to_dir)
    file_name = input("Enter file name like default(default-store): ")
    func_name = input("Enter function name like useDefaultStore: ")
    if file_name == "":
        print(colored("File name is required", "red"))
        exit()
    file_path = path_to_selected_dir + "/" + file_name + "-store.ts"
    with open(layout_path, "r") as f:
        layout = f.read()
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(layout)
                print(colored("File created: " + file_path, "green"))
    os.system(f"sed -i -e 's/default/{file_name}/g' '{file_path}' ")
    os.system(f"sed -i -e 's/useDefaultStore/{func_name}/g' '{file_path}' ")
    os.system(f"bat {file_path}")
