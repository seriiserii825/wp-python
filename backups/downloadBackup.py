import os
from urllib.parse import urlparse
from termcolor import colored


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
