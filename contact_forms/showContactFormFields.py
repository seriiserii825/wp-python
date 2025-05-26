from classes.MyTable import MyTable


def showContactFormFields(all_fields, required_fields, submited_fields):
    # sort submited_fields by required_fields
    sorted_submited_fields = []
    for field in all_fields:
        if field in submited_fields:
            sorted_submited_fields.append(field)
    sorted_submited_fields += [field for field in submited_fields if field not in all_fields]

    table_title = "Contact Form Fields"
    table_columns = ["All fields", "Required fields", "Submitted fields"]
    table_rows = []
    for field in sorted_submited_fields:
        if field in required_fields:
            table_rows.append([field, field, field])
        else:
            table_rows.append([field, '[red]No required', field])
    my_table = MyTable()
    my_table.show(table_title, table_columns, table_rows)
    # richTable(table_title, table_columns, table_rows)
