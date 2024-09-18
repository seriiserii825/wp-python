import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from backups.getLoginUrl import getLoginUrl
from backups.waitForCaptcha import waitForCaptcha
from utils.getProjects import getProjects


def restoreBackupInChrome():
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
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")))
    ai1wm_backup_dots = driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")
    ai1wm_backup_dots.click()
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-restore")))
    ai1wm_backup_restore = driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-restore")
    ai1wm_backup_restore.click()
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-import-modal-actions .ai1wm-button-green")))
    button_green = driver.find_element(By.CSS_SELECTOR, ".ai1wm-import-modal-actions .ai1wm-button-green")
    button_green.click()
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-import-modal-content-done")))
    time.sleep(1)
    driver.close()
    driver = webdriver.Chrome(service=service, options=options)
    sitem_login = f"{project_url}"
    while True:
        req = requests.get(sitem_login)
        if req.status_code != requests.codes['ok']:
            sitem_login = f"{project_url}/wp-admin"
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
    save_permalink_url = f"{project_url}/wp-admin/options-permalink.php"
    driver.get(save_permalink_url)
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#submit")))
    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit_button.click()
    plugins_url = f"{project_url}/wp-admin/plugins.php"
    driver.get(plugins_url)
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#activate-wps-hide-login")))
    wps_hide_login = driver.find_element(By.CSS_SELECTOR, "#activate-wps-hide-login")
    wps_hide_login.click()
    driver.close()

