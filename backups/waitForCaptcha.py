import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def waitForCaptcha(driver):
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".aiowps-captcha-answer")))
        aiowps_captcha_answer = driver.find_element(By.CSS_SELECTOR, ".aiowps-captcha-answer")
        if aiowps_captcha_answer:
            time.sleep(10)
    except TimeoutException:
        return
