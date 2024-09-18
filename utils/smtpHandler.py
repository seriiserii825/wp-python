import time
from smtp.apiSection import apiSection
from smtp.findOrCreateProject import findOrCreateProject
from smtp.loginSmtp import loginSmtp
from selenium.webdriver.support import expected_conditions as EC
import smtp.settings

def smtpHandler():
    google_console_url = "https://console.cloud.google.com/home/dashboard"
    smtp.settings.driver.get(google_console_url)
    try:
        loginSmtp()
    except:
        print('already logged in')
        findOrCreateProject()
        apiSection()
        # WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.purview-picker-create-project-button")))
        # create_project_button = driver.find_element(By.CSS_SELECTOR, "button.purview-picker-create-project-button")
        # create_project_button.click()
        # print('create project')
        # # mat-mdc-input-element
        # WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "proj-name-id-input input.mat-mdc-input-element")))
        # search_input = driver.find_element(By.CSS_SELECTOR, "proj-name-id-input input.mat-mdc-input-element")
        # print(f"search_input: {search_input}")
        # search_input.clear()
        # search_input.send_keys(project_title)
        # # projtest-create-form-submit
        # WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.projtest-create-form-submit")))
        # create_project_button = driver.find_element(By.CSS_SELECTOR, "button.projtest-create-form-submit")
        # time.sleep(2)
        # create_project_button.click()


    # login_element.send_keys(project_login)
    # password_element = driver.find_element(By.ID, "user_pass")
    # password_element.send_keys(project_password)
    # login_button = driver.find_element(By.ID, "wp-submit")
    # login_button.click()
    # backups_url = f"{project_url}/wp-admin/admin.php?page=ai1wm_backups"
    # driver.get(backups_url)
    # WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")))
    # ai1wm_backup_dots = driver.find_element(By.CSS_SELECTOR, "table.ai1wm-backups tr:nth-of-type(2) .ai1wm-backup-dots")
    # ai1wm_backup_dots.click()
    time.sleep(10000)
