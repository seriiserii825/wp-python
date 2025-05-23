from rich.console import Console
from rich.table import Table

class MyTable:
    """
    table_title = "Contact Form Fields"
    table_columns = ["All fields", "Required fields", "Submitted fields"]
    table_rows = []
    for field in sorted_submited_fields:
        if field in required_fields:
            table_rows.append([field, field, field])
        else:
            table_rows.append([field, '[red]No required', field])
    """
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
        

