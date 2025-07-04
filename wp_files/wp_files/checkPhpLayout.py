import os

from termcolor import colored


def checkPhpLayout(layout_path):
    if not os.path.exists(layout_path):
        # create this file
        print(colored("Creating php layout file...", "green"))
        dir_path = os.path.dirname(layout_path)
        os.system(f"mkdir -p {dir_path}")
        os_command = f"touch {layout_path}"
        os.system(os_command)
        with open(layout_path, "w") as f:
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
