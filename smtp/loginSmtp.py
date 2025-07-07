from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import smtp.settings
from utils.getGoogleData import getGoogleData


def loginSmtp():
    driver = smtp.settings.driver
    google_data = getGoogleData()
    login = google_data["login"]
    second_login = google_data["password"]
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    email_element = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    WebDriverWait(driver, 3000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    email_element = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_element.send_keys(login)
    WebDriverWait(driver, 3000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierNext button"))
    )
    next_button = driver.find_element(By.CSS_SELECTOR, "#identifierNext button")
    next_button.click()
    WebDriverWait(driver, 3000).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#password input[type='password']")
        )
    )
    password_element = driver.find_element(
        By.CSS_SELECTOR, "#password input[type='password']"
    )
    password_element.send_keys(second_login)
    WebDriverWait(driver, 3000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#passwordNext button"))
    )
    next_button = driver.find_element(By.CSS_SELECTOR, "#passwordNext button")
    next_button.click()
    print("login")
