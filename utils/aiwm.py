#!/usr/bin/python3
import os
from termcolor import colored
from urllib.parse import urlparse
from pick import pick
from pyfzf.pyfzf import FzfPrompt
import glob

from libs.listDir import listDir
from libs.listFiles import listFiles
from libs.select import selectOne
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory
fzf = FzfPrompt()

is_installed_plugins = os.path.exists("../../plugins/all-in-one-wp-migration");
if not is_installed_plugins:
    os.system("wp plugin install ~/Documents/plugins-wp/all-in-one-wp-migration-7-79.zip --activate")

is_installed_unlimited = os.path.exists("../../plugins/all-in-one-wp-migration-unlimited-extension");
if not is_installed_unlimited:
    os.system("wp plugin install ~/Documents/plugins-wp/unlimited/all-in-one-wp-migration-unlimited-extension-2.51.zip --activate")

def aiwmFunc():
    def listBackup():
        os.system("wp ai1wm list-backups")

    def createAndCopyToMnt():
        directory_exists = os.path.isdir('/mnt/Projects')
        if directory_exists:
            path_to_dir = '/mnt/Projects'
            listDir(path_to_dir)
            selected_dir = createOrChooseDirectory(path_to_dir)
            path_to_selected_dir = path_to_dir + "/" + selected_dir
            listDir(path_to_selected_dir)
            selected_project = createOrChooseDirectory(path_to_selected_dir)
            path_to_selected_dir = path_to_selected_dir + "/" + selected_project
            makeBackup(path_to_selected_dir)
            listFiles(path_to_selected_dir)
        else:
            exit(colored("Directory /mnt/Projects not exists!", "red"))

    def makeBackup(path_to_project=''):
        listBackup()
        os.system("wp ai1wm backup")
        list_of_files = glob.glob('../../ai1wm-backups/*.wpress')
        if not list_of_files:
            backup_files = os.listdir(".")
            for file in backup_files:
                if file.endswith('.wpress'):
                    os.system(f"cp {file} ~/Downloads")
                    if path_to_project != "":
                        os.system(f"cp {file} {path_to_project}")
            listBackup()
        else:
            latest_file = max(list_of_files, key=os.path.getctime)
            os.system(f"cp {latest_file} ~/Downloads")
            if path_to_project != "":
                os.system(f"cp {latest_file} {path_to_project}")
            listBackup()

    def restoreBackup():
        listBackup()
        os.chdir("../../ai1wm-backups")
        backup_files = os.listdir()

        title = 'Select plugins'
        backups_array = []
        selected_plugins = []
        for file in backup_files:
            if file.endswith('.wpress'):
                backups_array.append(file)
        selected = pick(backups_array, title, multiselect=False, min_selection_count=1)
        print(selected)
        for item in selected:
            selected_plugins.append(item)

        os.system(f"wp ai1wm restore {selected_plugins[0]}")

    def restoreFromDownloads():
        downloads_dir = os.path.expanduser("~/Downloads")
        backup_files = os.listdir(downloads_dir)
        title = 'Select files'
        backups_array = []
        selected_plugins = []
        for file in backup_files:
            if file.endswith('.wpress'):
                backups_array.append(file)
        selected = pick(backups_array, title, multiselect=False, min_selection_count=1)
        for item in selected:
            selected_plugins.append(item)
        os.system(f"cp ~/Downloads/{selected_plugins[0]} ../../ai1wm-backups")
        print(f"Selected file: {selected_plugins[0]}")
        os.system(f"wp ai1wm restore {selected_plugins[0]}")

    def downloadBackup():
        domain_url = input("Enter domain url: ")
        if domain_url == "":
            exit(colored("Domain url is empty!", "red"))
        domain = urlparse(domain_url).netloc
        domain = 'https://' + domain

        backup_file_name = input("Enter backup file name: ")
        if backup_file_name == "":
            exit(colored("Backup file name is empty!", "red"))

        os.chdir("../../ai1wm-backups")
        os.system(f"wget {domain}/wp-content/ai1wm-backups/{backup_file_name}")
        os.system(f"wp ai1wm restore {backup_file_name}")
        os.system("wp rewrite flush")

    def deleteBackup():
        os.chdir("../../ai1wm-backups")
        backup_files = os.listdir()

        title = 'Select files'
        backups_array = []
        selected_plugins = []
        for file in backup_files:
            if file.endswith('.wpress'):
                backups_array.append(file)
        selected = pick(backups_array, title, multiselect=True, min_selection_count=1)
        for item in selected:
            selected_plugins.append(item[0])
        for file in selected_plugins:
            os.system(f"rm -f {file}")

    def menu():
        print(colored("1) List", "green"))
        print(colored("2) Create", "yellow"))
        print(colored("2.1) Create and copy to mnt", "yellow"))
        print(colored("3) Restore", "blue"))
        print(colored("4) Restore from Downloads", "blue"))
        print(colored("5) Download Backup", "yellow"))
        print(colored("6) Delete backups", "red"))
        print(colored("7) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1":
            listBackup()
            menu()
        elif choice == "2":
            makeBackup()
            menu()
        elif choice == "2.1":
            createAndCopyToMnt()
            menu()
        elif choice == "3":
            restoreBackup()
            menu()
        elif choice == "4":
            restoreFromDownloads()
            menu()
        elif choice == "5":
            downloadBackup()
            menu()
        elif choice == "6":
            deleteBackup()
            menu()
        else:
            exit(colored("Goodbye!", "red"))

    menu()

