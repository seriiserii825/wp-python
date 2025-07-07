import os


def orderFiles(dir_path):
    current_path = os.getcwd()
    os.chdir(dir_path)
    backup_files = os.listdir()
    #sort by ctime in reverse order
    backup_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
    os.chdir(current_path)
    return backup_files
