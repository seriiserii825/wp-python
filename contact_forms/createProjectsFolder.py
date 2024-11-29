import os


def createProjectsFolder():
    ROOT_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    # create in root in contact_forms folder projects if not exists
    projects_path = os.path.join(ROOT_DIR, "contact_forms/projects")
    if not os.path.exists(projects_path):
        os.makedirs(projects_path)

    # get root folter directory name where script is executed
    current_dir = os.getcwd()
    # get last folder name
    folder_name = os.path.basename(current_dir)
    # create project folder
    project_folder = os.path.join(projects_path, folder_name)
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
    return project_folder

