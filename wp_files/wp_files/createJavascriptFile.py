import os

from termcolor import colored

from wp_files.wp_files.checkJsLayout import checkJsLayout
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory


def createJsFile():
    js_layout_path='template-parts/layouts/js-layout.ts'
    checkJsLayout(js_layout_path)
    path_to_dir = "src/js/modules"
    selected_dir = createOrChooseDirectory(path_to_dir)
    path_to_selected_dir = path_to_dir + "/" + selected_dir
    print(f"Selected dir: {path_to_selected_dir}")
    file_name = input("Enter file name like for function myFunc: ")
    if file_name == '':
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
                print(colored("File created: "+file_path, "green"))
    os.system(f"sed -i -e 's/jsLayout/{file_name}/g' '{file_path}' ")
    os.system(f"bat {file_path}")
