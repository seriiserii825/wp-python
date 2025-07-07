import os
import time

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from classes.Project import Project


class MySelenium():
    def __init__(self):
        self.service = Service(executable_path='/usr/bin/chromedriver')
        self.options = webdriver.ChromeOptions() 
        self.options.add_argument("user-data-dir=/home/serii/.config/google-chrome/My-profile") #Path to your chrome profile
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        current_dir_path = os.getcwd()
        self.theme_name = os.path.basename(current_dir_path)
        self.pr = Project(self.theme_name)
        self.project = self.pr.getProject()
        self.project_login = self.project['login']
        self.project_password = self.project['password']
        self.project_url = self.project['url']
        self.sitem_login = self.pr.getLoginUrl(False)

    def every_downloads_chrome(self, driver):
        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")
        return driver.execute_script("""
            const items = document.querySelector('downloads-manager')
                .shadowRoot.getElementById('downloadsList').items;
            if (items.every(e => e.state === "COMPLETE"))
                return items.map(e => e.fileUrl || e.file_url);
        """)

    def loginToSite(self):
        while True:
            req = requests.get(self.sitem_login)
            if req.status_code != requests.codes['ok']:
                self.sitem_login = f"{self.project_url}/wp-admin"
                break
            else:
                break

    def makeBackupInChrome(self):
        self.loginToSite()
        self.driver.get(self.sitem_login)
        self.waitForCaptcha()
        login_element = self.driver.find_element(By.ID, "user_login")
        login_element.send_keys(self.project_login)
        password_element = self.driver.find_element(By.ID, "user_pass")
        password_element.send_keys(self.project_password)
        login_button = self.driver.find_element(By.ID, "wp-submit")
        login_button.click()
        backups_url = f"{self.project_url}/wp-admin/admin.php?page=ai1wm_export"
        self.driver.get(backups_url)
        WebDriverWait(self.driver, 30000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-button-export")))
        ai1wm_backup_dots = self.driver.find_element(By.CSS_SELECTOR, ".ai1wm-button-export")
        ai1wm_backup_dots.click()
        WebDriverWait(self.driver, 30000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ai1wm-export-file")))
        ai1wm_backup_restore = self.driver.find_element(By.CSS_SELECTOR, "#ai1wm-export-file")
        time.sleep(2)
        ai1wm_backup_restore.click()
        WebDriverWait(self.driver, 3000000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-modal-container .ai1wm-button-green")))
        button_green = self.driver.find_element(By.CSS_SELECTOR, ".ai1wm-modal-container .ai1wm-button-green")
        button_green.click()
        WebDriverWait(self.driver, 120, 1).until(self.every_downloads_chrome)
        self.driver.close()
        time.sleep(10000000)

    def waitForCaptcha(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".aiowps-captcha-answer")))
            aiowps_captcha_answer = self.driver.find_element(By.CSS_SELECTOR, ".aiowps-captcha-answer")
            if aiowps_captcha_answer:
                time.sleep(10)
        except TimeoutException:
            return

    def restoreBackupInChrome(self):
        self.loginToSite()
        self.driver.get(self.sitem_login)
        self.waitForCaptcha()
        login_element = self.driver.find_element(By.ID, "user_login")
        login_element.send_keys(self.project_login)
        password_element = self.driver.find_element(By.ID, "user_pass")
        password_element.send_keys(self.project_password)
        login_button = self.driver.find_element(By.ID, "wp-submit")
        login_button.click()
        backups_url = f"{self.project_url}/wp-admin/admin.php?page=ai1wm_backups"
        self.driver.get(backups_url)
        WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")))
        ai1wm_backup_dots = self.driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")
        ai1wm_backup_dots.click()
        WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-restore")))
        ai1wm_backup_restore = self.driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-restore")
        ai1wm_backup_restore.click()
        WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-import-modal-actions .ai1wm-button-green")))
        button_green = self.driver.find_element(By.CSS_SELECTOR, ".ai1wm-import-modal-actions .ai1wm-button-green")
        button_green.click()
        WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ai1wm-import-modal-content-done")))
        time.sleep(1)
        self.driver.close()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.loginToSite()
        self.driver.get(self.sitem_login)
        self.waitForCaptcha()
        login_element = self.driver.find_element(By.ID, "user_login")
        login_element.send_keys(self.project_login)
        password_element = self.driver.find_element(By.ID, "user_pass")
        password_element.send_keys(self.project_password)
        login_button = self.driver.find_element(By.ID, "wp-submit")
        login_button.click()
        save_permalink_url = f"{self.project_url}/wp-admin/options-permalink.php"
        self.driver.get(save_permalink_url)
        WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#submit")))
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#submit")
        submit_button.click()
        plugins_url = f"{self.project_url}/wp-admin/plugins.php"
        self.driver.get(plugins_url)
        WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#activate-wps-hide-login")))
        wps_hide_login = self.driver.find_element(By.CSS_SELECTOR, "#activate-wps-hide-login")
        wps_hide_login.click()
        self.driver.close()

    def deleteBackupInChrome(self):
        self.loginToSite()
        self.driver.get(self.sitem_login)
        self.waitForCaptcha()
        login_element = self.driver.find_element(By.ID, "user_login")
        login_element.send_keys(self.project_login)
        password_element = self.driver.find_element(By.ID, "user_pass")
        password_element.send_keys(self.project_password)
        login_button = self.driver.find_element(By.ID, "wp-submit")
        login_button.click()
        backups_url = f"{self.project_url}/wp-admin/admin.php?page=ai1wm_backups"
        self.driver.get(backups_url)
        number_of_backups = input("[green]Enter number of backups to delete: ")
        if number_of_backups == "":
            exit("[red]Number of backups is empty!")
        print(f"Number of backups: {number_of_backups}")
        for i in range(int(number_of_backups)):
            WebDriverWait(self.driver, 300000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:last-of-type .ai1wm-backup-dots")))
            ai1wm_backup_dots = self.driver.find_element(By.CSS_SELECTOR, f"table.ai1wm-backups tr:nth-of-type({number_of_backups}) .ai1wm-backup-dots")
            ai1wm_backup_dots.click()
            WebDriverWait(self.driver, 300000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-delete")))
            ai1wm_backup_delete = self.driver.find_element(By.CSS_SELECTOR, f"table.ai1wm-backups tr:nth-of-type({number_of_backups}) .ai1wm-backup-delete")
            ai1wm_backup_delete.click()
            WebDriverWait(self.driver, 1000000).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            time.sleep(3)

