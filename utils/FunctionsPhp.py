from pathlib import Path

from classes.ThemePathFromFile import ThemePathFromFile


class FunctionsPhp:
    path = Path.cwd()
    theme_dir_path = ThemePathFromFile.get_theme_path()
    print(f"theme_dir_path from functions.php: {theme_dir_path}")

    @classmethod
    def get_functions_php_path(cls):
        return f"{cls.theme_dir_path}/functions.php"

    @classmethod
    def comment_autoload_in_functions_php(cls):
        functions_php_path = f"{cls.theme_dir_path}/functions.php"
        if Path(functions_php_path).exists():
            with open(functions_php_path, 'r') as file:
                lines = file.readlines()
            with open(functions_php_path, 'w') as file:
                for line in lines:
                    if "autoload" in line:
                        file.write(f"// {line}")
                    else:
                        file.write(line)
            print("[green]Autoload commented in functions.php")
        else:
            print("[red]functions.php not found")
