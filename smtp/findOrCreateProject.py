import smtp.settings
import time
from utils.checkElem import checkElem
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def findOrCreateProject():
    driver = smtp.settings.driver
    print('findOrCreateProject')
    button = checkElem("button.cfc-switcher-button")
    print(f"button: {button}")
    checkElem("button.cfc-switcher-button", click=True)
    table_rows = 'table.cfc-table-element tbody tr'
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.CSS_SELECTOR, table_rows)))
    rows = driver.find_elements(By.CSS_SELECTOR, table_rows)
    for row in rows:
        project_title = smtp.settings.project_title
        project_name = row.find_element(By.CSS_SELECTOR, 'a.cfc-purview-picker-list-name-link')
        print(f"project_title: {project_title}")
        print(f"project_name: {project_name}")
        project_name_text = project_name.text
        print(f"project_name_text: {project_name_text}")
        if project_title == project_name_text:
            project_name.click()
            print('project found')
            break
        else:
            print('create project')
            create_project_button = driver.find_element(By.CSS_SELECTOR, "button.purview-picker-create-project-button")
            create_project_button.click()
            search_input = driver.find_element(By.CSS_SELECTOR, "proj-name-id-input input.mat-mdc-input-element")
            search_input.clear()
            search_input.send_keys(project_title)
            create_project_button = driver.find_element(By.CSS_SELECTOR, "button.projtest-create-form-submit")
            time.sleep(2)
            create_project_button.click()
