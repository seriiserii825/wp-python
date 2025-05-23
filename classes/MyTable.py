from rich.console import Console
from rich.table import Table

class MyTable:
    def show(self,title, columns, rows):
        """
        Show a table with the given title, columns, and rows.
        """
        table = Table(title=title)

        for column in columns:
            table.add_column(column, style="magenta", no_wrap=True)

        for row in rows:
            table.add_row(*map(str, row))

        console = Console()
        console.print(table)
        

