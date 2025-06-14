from classes.MyTable import MyTable
from contact_forms.getRandomFields import getRandomFields


def showRandomFields():
    random_fields = getRandomFields()
    random_fields = sorted(random_fields, key=lambda k: k['name'])
    table_title = "Random Fields"
    table_columns = ["Field", "Values"]
    table_rows = []
    for random_field in random_fields:
        values = ', '.join(random_field['value'])
        table_rows.append([random_field['name'], values])
    MyTable.show(table_title, table_columns, table_rows)
