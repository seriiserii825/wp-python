from classes.MyTable import MyTable


class SectionMenu:
    rows_count = 0

    @staticmethod
    def display():
        """
        Display the main menu options.
        """
        columns = ["Index", "Option"]
        rows = [
            ["1", "Page"],
            ["2", "Custom Post Type"],
            ["3", "Taxonomy"],
            ["4", "Exit"],
        ]

        SectionMenu.rows_count = 0
        SectionMenu.rows_count += len(rows)

        tb = MyTable()
        tb.show("Main Menu", columns, rows)

    @staticmethod
    def choose_option():
        """
        Prompt the user to choose an option from the menu.
        """
        while True:
            try:
                count_range = "Please enter a number"
                f"between 1 and {SectionMenu.rows_count}: "
                choice = int(input(count_range))
                if choice in range(1, SectionMenu.rows_count + 1):
                    return choice
                else:
                    print(
                        f"[red]Invalid input."
                        f"Please enter a number between 1 and {SectionMenu.rows_count}."
                    )
            except ValueError:
                print("[red] Input must be a number. Please try again.[/red]")
