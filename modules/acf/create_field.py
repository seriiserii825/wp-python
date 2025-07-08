from acf.acf_utils.section.SectionMenu import SectionMenu
from classes.Acf.Field import Field


def create_field():
    headers = ['Index', 'Option']
    field_types = Field.get_field_types()
    rows = [[f"{i}", field_type] for i, field_type in enumerate(field_types)]

    SectionMenu.display("Create Field", headers, rows)
    choice = SectionMenu.choose_option()
    print(f"choice: {choice}")
