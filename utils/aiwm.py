#!/usr/bin/python3
import os

from termcolor import colored

from backups.createAndCopyToMnt import createAndCopyToMnt
from backups.deleteBackup import deleteBackup
from backups.deleteBackupInChrome import deleteBackupInChrome
from backups.downloadBackup import downloadBackup
from backups.listBackup import listBackup
from backups.makeBackup import makeBackup
from backups.makeBackupInChrome import makeBackupInChrome
from backups.restoreBackup import restoreBackup
from backups.restoreBackupInChrome import restoreBackupInChrome
from backups.restoreFromDownloads import restoreFromDownloads
from classes.Backup import Backup

is_installed_plugins = os.path.exists("../../plugins/all-in-one-wp-migration");
if not is_installed_plugins:
    os.system("wp plugin install ~/Documents/plugins-wp/all-in-one-wp-migration-7-79.zip --activate")

is_installed_unlimited = os.path.exists("../../plugins/all-in-one-wp-migration-unlimited-extension");
if not is_installed_unlimited:
    os.system("wp plugin install ~/Documents/plugins-wp/unlimited/all-in-one-wp-migration-unlimited-extension-2.51.zip --activate")

def aiwmFunc():

    def menu():
        print(colored("1) List", "green"))
        print(colored("2) Create", "yellow"))
        print(colored("2.1) Create and copy to mnt", "yellow"))
        print(colored("2.2) Create backup on server", "yellow"))
        print(colored("3) Restore", "blue"))
        print(colored("4) Restore from Downloads", "blue"))
        print(colored("5) Restore in Browser", "blue"))
        print(colored("5.1) Delete in Browser", "red"))
        print(colored("6) Download Backup", "yellow"))
        print(colored("7) Delete backups", "red"))
        print(colored("8) Exit", "red"))

        choice = input("Make your choice:")
        if choice == "1":
            backup = Backup()
            backup.listBackup()
            menu()
        elif choice == "2":
            backup = Backup()
            backup.deleteMore3Backups()
            backup.makeBackup()
            backup.listBackup()
            menu()
        elif choice == "2.1":
            bp = Backup()
            bp.createAndCopyToMnt()
        elif choice == "2.2":
            bp = Backup()
            bp.makeBackupInChrome()
            menu()
        elif choice == "3":
            bp = Backup()
            bp.restoreBackup()
            menu()
        elif choice == "4":
            bp = Backup()
            bp.restoreFromDownloads()
            menu()
        elif choice == "5":
            restoreBackupInChrome()
            menu()
        elif choice == "5.1":
            deleteBackupInChrome()
            menu()
        elif choice == "6":
            downloadBackup()
            menu()
        elif choice == "7":
            deleteBackup()
            menu()
        else:
            exit(colored("Goodbye!", "red"))

    menu()

