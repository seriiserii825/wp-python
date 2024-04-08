import subprocess
import os

def init():
    user = os.getenv('USER')
    path_to_wp_init = "/home/" + str(user) + "/Documents/python/wp-python/wp-init.sh"
    subprocess.call(path_to_wp_init, shell=True)
