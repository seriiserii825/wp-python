from rich.console import Console
from rich.table import Table

def richTable(title, columns, rows):
    table = Table(title=title)

    for column in columns:
        table.add_column(column, style="magenta", no_wrap=True)
    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)
    

