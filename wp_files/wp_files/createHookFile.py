import os
from termcolor import colored
from libs.listFiles import listFiles

def createHookFile():
    layout_path='template-parts/layouts/default-hook.ts'
    path_to_dir = "src/vue/hooks"
    path_to_selected_dir = path_to_dir
    listFiles(path_to_dir)
    file_name = input("Enter file name like useDefault: ")
    if file_name == '':
        print(colored("File name is required", "red"))
        exit()
    file_path = path_to_selected_dir + "/" + file_name + ".ts"
    with open(layout_path, "r") as f:
        layout = f.read()
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(layout)
                print(colored("File created: "+file_path, "green"))
    os.system(f"sed -i -e 's/useDefault/{file_name}/g' '{file_path}' ")
    os.system(f"bat {file_path}")
