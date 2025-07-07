from typing import List
from rich.console import Console
from rich.table import Table


class MyTable:
    def __init__(self):
        self.console = Console()

    def show(self, title: str, columns: List[str], rows, *, row_styles=None):
        """
        Print a Rich table.

        Parameters
        ----------
        title : str
            Table title.
        columns : list[dict]
            Each dict must have keys "title" and "style".
        rows : list[list[str]]
            2‑D list of cell values.
        row_styles : dict[int, str] | None
            Map of row index → Rich style string.
            Example: {0: "bold green", 3: "bright_red"}
            (row index is **zero‑based** inside this method)
        """
        row_styles = row_styles or {}

        table = Table(title=title, show_lines=False, expand=False)

        for col in columns:
            table.add_column(col)

        for _, row in enumerate(rows):
            table.add_row(*row)

        self.console.print(table)
