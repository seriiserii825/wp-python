import os
from termcolor import colored
from libs.listFilesWithPrefix import listFilesWithPrefix
from wp_files.wp_files.checkPhpPageLayout import checkPhpPageLayout
def createPhpPage():
    path_to_page_layout = 'template-parts/layouts/php-page.php'
    checkPhpPageLayout(path_to_page_layout)
    listFilesWithPrefix("./", ["page-", "single-"])
    file_name = input("Enter file name, "+ colored("like", "red") +" page-servizi or single-servizi: ")
    if file_name == '':
        print(colored("File name is required", "red"))
        exit()
    else:
        with open(path_to_page_layout, "r") as f:
            layout = f.read()
            file_path = file_name + ".php"
            if os.path.exists(file_path):
                print(colored("File exists", "red"))
                exit()
            else:
                with open(file_path, "w") as f:
                    f.write(layout)
                    print(colored("File created: "+file_path, "green"))
        os.system(f"bat {file_path}")
