import os
from termcolor import colored
from libs.listFiles import listFiles
from wp_files.wp_files.checkRestApiLayout import checkRestApiLayout

def createRestApiFile():
    layout_path='template-parts/layouts/rest-api-layout.php'
    checkRestApiLayout(layout_path)
    path_to_dir = "api"
    listFiles(path_to_dir)
    file_name = input("Enter file name like products: ")
    if file_name == '':
        print(colored("File name is required", "red"))
        exit()
    file_path = path_to_dir + "/" + file_name + "-api.php"
    with open(layout_path, "r") as f:
        layout = f.read()
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(layout)
                print(colored("File created: "+file_path, "green"))
    os.system(f"sed -i -e 's/events/{file_name}/g' '{file_path}' ")
    os.system(f"bat {file_path}")
