import os
def formToFiles(form):
    form_id = form['id']
    form_html_path = form['folder_path']+f"/html.txt"
    command = f"wp post meta get {form_id} _form --allow-root > {form_html_path}"
    os.system(command)

    form_file_path = form['folder_path']+f"/mail.txt"
    command = f"wp post meta get {form_id} _mail --allow-root > {form_file_path}"
    os.system(command)
    return {
            "html": form_html_path,
            "mail": form_file_path
            }

