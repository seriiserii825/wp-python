import os
from termcolor import colored
from libs.camelToKebabCase import camelToKebabCase
from libs.select import selectOne
from wp_files.wp_files.checkVueLayout import checkVueLayout
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory

def createVueFile():
    layout_path='template-parts/layouts/default.vue'
    checkVueLayout(layout_path)
    dir_select = selectOne(["views", "components"])
    if dir_select == "views":
        path_to_dir = "src/vue/views"
        path_to_selected_dir = path_to_dir
    else:
        path_to_dir = "src/vue/components"
        selected_dir = createOrChooseDirectory(path_to_dir)
        path_to_selected_dir = path_to_dir + "/" + selected_dir
    print(f"Selected dir: {path_to_selected_dir}")
    file_name = input("Enter file name, for view AppView, for components MyApp: ")
    if file_name == '':
        print(colored("File name is required", "red"))
        exit()
    file_path = path_to_selected_dir + "/" + file_name + ".vue"
    with open(layout_path, "r") as f:
        layout = f.read()
        if os.path.exists(file_path):
            print(colored("File exists", "red"))
            exit()
        else:
            with open(file_path, "w") as f:
                f.write(layout)
                print(colored("File created: "+file_path, "green"))
    class_name = camelToKebabCase(file_name)
    os.system(f"sed -i -e 's/vue/{class_name}/g' '{file_path}' ")
    os.system(f"bat {file_path}")
