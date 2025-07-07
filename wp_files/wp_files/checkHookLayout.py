import os

from termcolor import colored


def checkHookLayout(layout_path):
    if not os.path.exists(layout_path):
        print(colored("Creating hook layout file...", "green"))
        with open(layout_path, 'w') as f:
            layout_code = """
                export const useDefault = () => {

                };
            """
            f.write(layout_code)
    else:
        print(colored("Layout hook exists", "blue"))
