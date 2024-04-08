import os
from termcolor import colored


def checkCssLayout(scss_layout_path):
    if not os.path.exists(scss_layout_path):
        # create this file
        print(colored("Creating scss layout file...", "green"))
        with open(scss_layout_path, 'w') as f:
            layout_code = """
            .home {
              &__title{}
            }
            """
            f.write(layout_code)
    else:
        print(colored("Layout scss exists", "blue"))
