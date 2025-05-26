# get path to this folder and add it to the path
import os
form_html = 'form.txt'
form_html_path = os.path.join(os.path.dirname(__file__), form_html)
form_file = 'submit-form.txt'
form_file_path = os.path.join(os.path.dirname(__file__), form_file)
contact_forms_csv = 'contact_forms.csv'
contact_forms_csv_path = os.path.join(os.path.dirname(__file__), contact_forms_csv)
