import os
import csv
from termcolor import colored

def getGoogleData():
    ROOT_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    # print(ROOT_DIR)
    csv_file_path = os.path.join(ROOT_DIR, 'google-data.csv')
    if not os.path.exists(csv_file_path):
        print(colored("File google-data.csv does not exist", "red"))
        exit(1)
    data = {
            'login': '',
            'password': ''
            }
    with open(csv_file_path) as my_file:
        reader = csv.reader(my_file, delimiter ='|')
        for row in reader:
            data['login'] = row[0]
            data['password'] = row[1]
    return data

        
