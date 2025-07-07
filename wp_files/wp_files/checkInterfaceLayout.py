import os

from termcolor import colored


def checkInterfaceLayout(layout_path):
    if not os.path.exists(layout_path):
        print(colored("Creating inteface layout file...", "green"))
        with open(layout_path, 'w') as f:
            layout_code = """
              export interface IDefault {

              }
            """
            f.write(layout_code)
    else:
        print(colored("Layout inteface exists", "blue"))
