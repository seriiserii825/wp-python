from simple_term_menu import TerminalMenu
def selectOne(options):
    terminal_menu = TerminalMenu(options)
    # menu_entry_index = terminal_menu.show()
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]

# selectOne(getThemes())

def selectMultiple(options):
    terminal_menu = TerminalMenu(options,
                                 multi_select=True,
                                 show_multi_select_hint=True,
                                 show_search_hint=True,
                                 preview_command="bat --color=always {}", preview_size=0.75
                                 )
    menu_entry_indices = terminal_menu.show()
    # print(menu_entry_indices)
    # print(terminal_menu.chosen_menu_entries)
    return terminal_menu.chosen_menu_entries

