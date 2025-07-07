from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import colored

import smtp.settings
from utils.checkElem import checkElem


def apiSection():
    driver = smtp.settings.driver
    theme_name = smtp.settings.theme_name
    login = smtp.settings.login
    print("apiSection")
    print("burger menu")
    checkElem("#pcc-console-nav-container button", click=True)
    print("api service")
    if checkElem("a.cfc-console-nav-section-API_SECTION", click=True):
        print("library")
        checkElem("a#cfctest-section-nav-item-marketplace_api_library", click=True)
        print("gmail_selector")
        search_gmail_selector = "input[name='searchInput']"
        WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_gmail_selector))
        )
        search_gmail_input = driver.find_element(By.CSS_SELECTOR, search_gmail_selector)
        search_gmail_input.send_keys("Gmail API")
        # press Enter
        search_gmail_input.send_keys("\ue007")
        print("gmail link")
        checkElem("a.mp-search-results-list-item-link:first-of-type", click=True)
        print("create_credentials")
        checkElem("a[aria-label='Create credentials']", click=True)
        print("oauth_client")
        checkElem("input[value='OAUTH_CLIENT']", click=True)
        print("next_btn")
        checkElem("button.cfc-stepper-step-button", click=True)
        print("app_name")
        app_name_selector = "input[formcontrolname='displayName']"
        WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, app_name_selector))
        )
        app_name_input = driver.find_element(By.CSS_SELECTOR, app_name_selector)
        app_name_input.send_keys(theme_name)

        print("developer_email")
        developer_email_selector = "input[aria-label='Text field for emails']"
        WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, developer_email_selector))
        )
        developer_email_input = driver.find_element(
            By.CSS_SELECTOR, developer_email_selector
        )
        developer_email_input.send_keys(login)

        print("save_continue")
        checkElem("button.cfc-stepper-step-continue-button", click=True)

        print("enable btn")
        checkElem(".mp-details-cta-button-primary button", click=True)
    else:
        print(colored("api service not found", "red"))
