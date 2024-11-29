import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import colored
from selenium.webdriver.support import expected_conditions as EC

from backups.getLoginUrl import getLoginUrl
from backups.waitForCaptcha import waitForCaptcha
from utils.getProjects import getProjects


def deleteBackupInChrome():
    current_dir_path = os.getcwd()
    theme_name = os.path.basename(current_dir_path)
    print(f"Theme name: {theme_name}")
    project = getProjects(theme_name)
    project_login = project['login']
    project_password = project['password']
    project_url = project['url']
    print(f"Project url: {project_url}")
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/home/serii/.config/google-chrome/My-profile") #Path to your chrome profile
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    sitem_login = getLoginUrl(theme_name, False)
    while True:
        req = requests.get(sitem_login)
        if req.status_code != requests.codes['ok']:
            sitem_login = getLoginUrl(theme_name)
            break
        else:
            break
    driver.get(sitem_login)
    waitForCaptcha(driver)
    login_element = driver.find_element(By.ID, "user_login")
    login_element.send_keys(project_login)
    password_element = driver.find_element(By.ID, "user_pass")
    password_element.send_keys(project_password)
    login_button = driver.find_element(By.ID, "wp-submit")
    login_button.click()
    backups_url = f"{project_url}/wp-admin/admin.php?page=ai1wm_backups"
    driver.get(backups_url)
    number_of_backups = input("[green]Enter number of backups to delete: ")
    if number_of_backups == "":
        exit(colored("Number of backups is empty!", "red"))
    print(f"Number of backups: {number_of_backups}")
    for i in range(int(number_of_backups)):
        WebDriverWait(driver, 300000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:last-of-type .ai1wm-backup-dots")))
        ai1wm_backup_dots = driver.find_element(By.CSS_SELECTOR, f"table.ai1wm-backups tr:nth-of-type({number_of_backups}) .ai1wm-backup-dots")
        ai1wm_backup_dots.click()
        WebDriverWait(driver, 300000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-delete")))
        ai1wm_backup_delete = driver.find_element(By.CSS_SELECTOR, f"table.ai1wm-backups tr:nth-of-type({number_of_backups}) .ai1wm-backup-delete")
        ai1wm_backup_delete.click()
        WebDriverWait(driver, 1000000).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(3)

