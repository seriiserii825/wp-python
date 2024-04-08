import os
from termcolor import colored


def checkPhpComponentLayout(php_compnent_layout_path):
    if not os.path.exists(php_compnent_layout_path):
        # create this file
        print(colored("Creating php component layout file...", "green"))
        with open(php_compnent_layout_path, 'w') as f:
            layout_code = """
            <?php  function defaultComponent(){ ?>

            <?php } ?>
            """
            f.write(layout_code)
    else:
        print(colored("Layout for php component exists", "green"))
