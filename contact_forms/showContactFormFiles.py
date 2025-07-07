import os


def showContactFormFiles(form_files_paths):
    form_html = form_files_paths["html"]
    form_mail = form_files_paths["mail"]
    os.system(f"bat {form_html}")
    os.system(f"bat {form_mail}")
