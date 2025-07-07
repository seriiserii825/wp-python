import os

import contact_forms.contact_settins as contact_settings
from libs.selectWithFzf import selectWithFzf


def getContactForm(project_folder):
    csv_file = contact_settings.contact_forms_csv_path
    os.system(f"wp post list --post_type=wpcf7_contact_form --format=csv --allow-root > {csv_file}")
    result = []
    with open(csv_file, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if index == 0:
                continue
            fields = line.split(',')
            result.append(f"{fields[1]}-{fields[0]}")
    selected_form = selectWithFzf(result)
    #form folder name with underscores instead of spaces and lowercase

    replaced_symbols = [' ', '(', ')', '/', '\\', ':', '*', '?', '"', '<', '>',]
    form_name = selected_form.split('-')[0].lower()
    for symbol in replaced_symbols:
        form_name = form_name.replace(symbol, '-')
    form_id = selected_form.split('-')[1]
    form_folder_path = os.path.join(project_folder, form_name + '-' + form_id)
    if not os.path.exists(form_folder_path):
        os.makedirs(form_folder_path)
    print(f"Selected form: {form_name}-{form_id}")
    return {
            "id": form_id,
            "title": form_name,
            "folder_path": form_folder_path
            }
