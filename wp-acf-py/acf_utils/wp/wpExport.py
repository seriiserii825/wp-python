import os

def wpExport():
    os.system("rm -rf acf")
    os.system("wp acf export --all")
