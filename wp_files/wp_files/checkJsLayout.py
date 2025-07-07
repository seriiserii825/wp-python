import os

from termcolor import colored


def checkJsLayout(layout_path):
    if not os.path.exists(layout_path):
        print(colored("Creating js layout file...", "green"))
        with open(layout_path, "w") as f:
            layout_code = """
          export default function jsLayout() {}
            """
            f.write(layout_code)
    else:
        print(colored("Layout js exists", "blue"))
