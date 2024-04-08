import os
from termcolor import colored
from libs.listFiles import listFiles
from wp_files.wp_files.checkPhpComponentLayout import checkPhpComponentLayout
from wp_files.wp_files.createScssFile import createScssFile

def createPhpComponentFile():
    php_component_layout_path = 'template-parts/layouts/php-component.php'
    checkPhpComponentLayout(php_component_layout_path)
    path_to_functions_php = "functions.php"
    path_to_dir = "components"
    listFiles(path_to_dir)
    file_name = input("Enter file name, like myComponent: ")
    if file_name == '':
        print(colored("File name is required", "red"))
        exit()
    else:
        with open(php_component_layout_path, "r") as f:
            layout = f.read()
            file_path = path_to_dir + "/" + file_name + ".php"
            if os.path.exists(file_path):
                print(colored("File exists", "red"))
                exit()
            else:
                with open(file_path, "w") as f:
                    f.write(layout)
                    print(colored("File created: "+file_path, "green"))
        os.system(f"sed -i -e 's/defaultComponent/{file_name}/g' '{file_path}' ")
        os.system(f"bat {file_path}")
        with open(path_to_functions_php, "a") as f:
            f.write(f"\nrequire get_template_directory() . '/{file_path}';")
        os.system(f"bat {path_to_functions_php}")
        createScssFile('components', file_name)
