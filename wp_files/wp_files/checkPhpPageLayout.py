
import os

from termcolor import colored


def checkPhpPageLayout(php_page_layout_path):
    if not os.path.exists(php_page_layout_path):
        print(colored("Creating php page layout file...", "green"))
        with open(php_page_layout_path, 'w') as f:
            layout_code = """
<?php get_header(); ?>
<?php get_footer(); ?>
            """
            f.write(layout_code)
    else:
        print(colored("Layout for php page exists", "green"))
