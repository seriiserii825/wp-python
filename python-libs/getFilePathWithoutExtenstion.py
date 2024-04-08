import os


def getFilePathWithoutExtension(file_path):
    base_name = os.path.basename(file_path)  # Get the base name of the file
    file_name, file_extension = os.path.splitext(base_name)  # Split the file name and extension
    dir_name = os.path.dirname(file_path)  # Get the directory name
    return os.path.join(dir_name, file_name)  # Join directory name and file name without extension
