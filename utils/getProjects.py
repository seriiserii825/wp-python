import csv
import os

from termcolor import colored


def getProjects(theme_name):
    projects = ()
    ROOT_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    # print(ROOT_DIR)
    csv_file_path = os.path.join(ROOT_DIR, 'list.csv')
    with open(csv_file_path) as my_file:
        reader = csv.reader(my_file, delimiter =',')
        for row in reader:
            project = {
                    'title': row[0],
                    'login': row[1],
                    'password': row[2],
                    'url': row[3],
                    }
            if len(row) > 4:
                project['gestione'] = row[4]
            projects = projects + (project,)
    theme_is_in_projects = [project for project in projects if project['title'] == theme_name]
    if not theme_is_in_projects:
        print(colored("Theme is not in projects", "red"))
        exit(1)
    else:
        return theme_is_in_projects[0]
