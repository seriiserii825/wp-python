from pathlib import Path
from rich import print


class ThemePathToFile:
    path = Path.cwd()
    style_css_path = path / "style.css"
    if not style_css_path.exists():
        exit("[red]Please run this script from the root of your theme folder!")

    python_script_dir_path = Path(__file__).resolve().parent.parent
    print(f"python_script_dir_path: {python_script_dir_path}")
    theme_name = path.parts[-1]
    theme_dir_abs_path = path.resolve()
    print(f"theme_dir_abs_path: {theme_dir_abs_path}")
    theme_file_path = f"{python_script_dir_path}/wp_theme_path.txt"
    print(f"theme_file_path: {theme_file_path}")

    @classmethod
    def theme_path_to_file(cls):
        with open(cls.theme_file_path, 'w') as file:
            file.write(str(cls.theme_dir_abs_path))
        print(f"[green]Theme path saved to {cls.theme_file_path}")

