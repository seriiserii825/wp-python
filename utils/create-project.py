#!/usr/bin/python3
import os
import shutil
from distutils.dir_util import copy_tree
from termcolor import colored

def createProject():
    PROJECT_STARTER = '/home/serii/Local/lc-vite/app/public/wp-content/themes/bs-vite'
    project_name = input('Enter project name: ')
    project_name_underscore = project_name.replace('-', '_')

    directory_exists = os.path.isdir(project_name)

    if directory_exists:
        print(colored('Directory already exists', 'red'))
    else:
        copy_tree(PROJECT_STARTER, project_name)
        os.chdir(project_name)
        shutil.rmtree('.git')
# replace occurience
        command = f'find . -type f -exec sed -i "s/bs-vite/{project_name}/g" {{}} \\;'
        command2 = f'find . -type f -exec sed -i "s/bs_vite/{project_name_underscore}/g" {{}} \\;'
        os.system(command)
        print(f'replaced bs-vite with {project_name}')
        os.system(command2)
        print(f'replaced bs-vite with {project_name_underscore}')


