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


def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)
def makeBackupInChrome():
    current_dir_path = os.getcwd()
    theme_name = os.path.basename(current_dir_path)
    print(f"Theme name: {theme_name}")
    project = getProjects(theme_name)
    project_login = project['login']
    project_password = project['password']
    project_url = project['url']
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
    backups_url = f"{project_url}/wp-admin/admin.php?page=ai1wm_export"
    print(backups_url)
    driver.get(backups_url)
    WebDriverWait(driver, 30000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-button-export")))
    ai1wm_backup_dots = driver.find_element(By.CSS_SELECTOR, ".ai1wm-button-export")
    ai1wm_backup_dots.click()
    WebDriverWait(driver, 30000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ai1wm-export-file")))
    ai1wm_backup_restore = driver.find_element(By.CSS_SELECTOR, "#ai1wm-export-file")
    print(f"ai1wm_backup_restore: {ai1wm_backup_restore}")
    time.sleep(2)
    ai1wm_backup_restore.click()
    WebDriverWait(driver, 3000000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-modal-container .ai1wm-button-green")))
    button_green = driver.find_element(By.CSS_SELECTOR, ".ai1wm-modal-container .ai1wm-button-green")
    button_green.click()
    WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
    driver.close()
    time.sleep(10000000)

