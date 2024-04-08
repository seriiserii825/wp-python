import os
from termcolor import colored


def checkPhpLayout(layout_path):
    if not os.path.exists(layout_path):
        # create this file
        print(colored("Creating php layout file...", "green"))
        with open(layout_path, 'w') as f:
            layout_code = """
            <?php
            $home = get_field('home');
            ?>

            <div class="home">
            </div>
            """
            f.write(layout_code)
    else:
        print(colored("Layout for php exists", "green"))
