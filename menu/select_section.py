from classes.Acf.AcfMenu import AcfMenu
from classes.Acf.SelectSection import SelectSection


def select_section():
    SelectSection.init()

    SelectSection.show_all()
    # header = ["Index", "Option"]
    # rows = [["0", "Show All"], ["5", "Exit"]]
    # AcfMenu.display("ACF Menu", header, rows)
    # option = AcfMenu.choose_option()
    # if option == 0:
    #     SelectSection.show_all()
    # elif option == 5:
    #     exit()
