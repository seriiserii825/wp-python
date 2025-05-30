import os

from classes.WpCli import WpCli

def wpExport():
    wp_cli = WpCli()
    os.system("rm -rf acf")
    wp_cli.runWp("acf export --all")
