import os
import glob
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from urllib.parse import urlparse
from pick import pick
from termcolor import colored
from libs.listDir import listDir
from utils.getProjects import getProjects
from wp_files.wp_files.createOrChooseDirectory import createOrChooseDirectory
from libs.orderFiles import orderFiles

def listBackup():
    os.system("wp ai1wm list-backups")

def restoreBackupInChrome():
    current_dir_path = os.getcwd()
    theme_name = os.path.basename(current_dir_path)
    print(f"Theme name: {theme_name}")
    project = getProjects(theme_name)
    project_title = project['title']
    project_login = project['login']
    project_password = project['password']
    project_url = project['url']
    print(f"Project url: {project_url}")
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/home/serii/.config/google-chrome/My-profile") #Path to your chrome profile
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    sitem_login = f"{project_url}/gestione"
    driver.get(sitem_login)
    login_element = driver.find_element(By.ID, "user_login")
    login_element.send_keys(project_login)

    password_element = driver.find_element(By.ID, "user_pass")
    password_element.send_keys(project_password)

    login_button = driver.find_element(By.ID, "wp-submit")
    login_button.click()
    backups_url = f"{project_url}/wp-admin/admin.php?page=ai1wm_backups"
    driver.get(backups_url)
    ai1wm_backup_dots = driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")
    ai1wm_backup_dots.click()
    ai1wm_backup_restore = driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-restore")
    time.sleep(2)
    ai1wm_backup_restore.click()
    time.sleep(10000)

def makeBackupInChrome():
    current_dir_path = os.getcwd()
    theme_name = os.path.basename(current_dir_path)
    print(f"Theme name: {theme_name}")
    # exit()
    project = getProjects(theme_name)
    project_login = project['login']
    project_password = project['password']
    project_url = project['url']
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/home/serii/.config/google-chrome/My-profile") #Path to your chrome profile
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    sitem_login = f"{project_url}/gestione"
    driver.get(sitem_login)
    login_element = driver.find_element(By.ID, "user_login")
    login_element.send_keys(project_login)

    password_element = driver.find_element(By.ID, "user_pass")
    password_element.send_keys(project_password)

    login_button = driver.find_element(By.ID, "wp-submit")
    login_button.click()
    backups_url = f"{project_url}/wp-admin/admin.php?page=ai1wm_export"
    driver.get(backups_url)
    ai1wm_backup_dots = driver.find_element(By.CSS_SELECTOR, ".ai1wm-button-export")
    ai1wm_backup_dots.click()
    time.sleep(2)
    ai1wm_backup_restore = driver.find_element(By.CSS_SELECTOR, ".ai1wm-dropdown-menu li a")
    ai1wm_backup_restore.click()
    time.sleep(10000)


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
        sorted_files = orderFiles(path_to_selected_dir)
        makeBackup(path_to_selected_dir)
        print(colored(f"Backup file copied to {path_to_selected_dir}", "blue"))
        for file in sorted_files:
            print(file)
    else:
        exit(colored("Directory /mnt/Projects not exists!", "red"))
def makeBackup(path_to_project=''):
    listBackup()
    os.system("wp ai1wm backup")
    list_of_files = glob.glob('../../ai1wm-backups/*.wpress')
    latest_file = max(list_of_files, key=os.path.getctime)
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
    print(colored(f"Backup file: {latest_file}", "blue"))
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
    backup_files = orderFiles(downloads_dir)
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
    #sort by ctime in reverse order
    backup_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
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
