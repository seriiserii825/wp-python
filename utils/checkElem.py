from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import colored

import smtp.settings


def checkElem(selector, delay=3, click=False):
    driver = smtp.settings.driver
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element = driver.find_element(By.CSS_SELECTOR, selector)
        if click:
            element.click()
        else:
            return element
    except Exception:
        print(colored(f"Element not found: {selector}", "red"))
        return False
