from classes.Acf.AcfMenu import AcfMenu
from classes.Acf.SelectSection import SelectSection
from modules.acf.create_field import create_field


def select_section():
    SelectSection.init()

    SelectSection.show_all()
    header = ["Index", "Option"]
    rows = [["0", "Show All"], ["1", "Create"], ["5", "Exit"]]
    AcfMenu.display("ACF Menu", header, rows)
    option = AcfMenu.choose_option()
    if option == 0:
        SelectSection.show_all()
    elif option == 1:
        create_field()
    elif option == 5:
        exit()
