from typing import List

from classes.MyTable import MyTable


class AcfMenu():
    rows_count = 0

    @staticmethod
    def display(title: str, columns: List[str], rows: List[List[str]]):
        """
        Display the main menu options.
        """

        AcfMenu.rows_count = 0
        AcfMenu.rows_count += len(rows)

        tb = MyTable()
        tb.show(title, columns, rows)

    @staticmethod
    def choose_option():
        """
        Prompt the user to choose an option from the menu.
        """
        while True:
            try:
                count_range = "Please enter a number: "
                f"between 0 and {AcfMenu.rows_count - 1}: "
                choice = int(input(count_range))
                if choice in range(0, AcfMenu.rows_count):
                    return choice
                else:
                    print(
                        f"[red]Invalid input."
                        f"Enter a number between 0 and {AcfMenu.rows_count - 1}."
                    )
            except ValueError:
                print("[red] Input must be a number. Please try again.[/red]")
