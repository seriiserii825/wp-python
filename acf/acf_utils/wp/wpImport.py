import os


def wpImport():
    os.system("wp acf clean")
    os.system("wp acf import --all")
