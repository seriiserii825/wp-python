import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.getGoogleData import getGoogleData
from utils.getProjects import getProjects

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=/home/serii/.config/google-chrome/My-profile") #Path to your chrome profile
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
service = Service(executable_path='/usr/bin/chromedriver')
# driver = webdriver.Chrome(service=service, options=options)

google_data = getGoogleData()
login = google_data['login']

current_dir_path = os.getcwd()
theme_name = os.path.basename(current_dir_path)
print(f"Theme name: {theme_name}")
project = getProjects(theme_name)
project_title = project['title']
