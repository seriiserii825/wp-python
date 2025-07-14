from pathlib import Path
from rich import print


class ThemePathFromFile:
    python_script_dir_path = Path(__file__).resolve().parent.parent
    # print(f"python_script_dir_path: {python_script_dir_path}")
    theme_file_path = f"{python_script_dir_path}/wp_theme_path.txt"
    # print(f"theme_file_path: {theme_file_path}")

    @classmethod
    def get_theme_path(cls):
        if not Path(cls.theme_file_path).exists():
            print(
                "[red]Theme path file does not exist.")
            return None
        with open(cls.theme_file_path, 'r') as file:
            theme_path = file.read().strip()
        return theme_path
