from rich import print
from rich.console import Console

from contact_forms.checkRandomFields import checkRandomFields
from contact_forms.getRandomFields import getRandomFields
from contact_forms.showRandomFields import showRandomFields
console = Console()
from contact_forms.createProjectsFolder import createProjectsFolder
from contact_forms.formToFiles import formToFiles
from contact_forms.generateEmail import generateEmail
from contact_forms.getContactForm import getContactForm
from contact_forms.getRequiredFileds import getRequiredFileds
from contact_forms.getSubmitedFields import getSubmitedFields
from contact_forms.showContactFormFields import showContactFormFields
from contact_forms.showContactFormFiles import showContactFormFiles

def submenu(form_files_paths, all_fields, required_fields, submited_fields, project_folder):
    print("[blue]1. Show contact form fields")
    print("[green]2. Show files")
    print("[blue]3. Show random_fields")
    print("[yellow]4. Generate email")
    print("[red]5. Exit")

    option = input("Select an option: ")
    if option == "1":
        showContactFormFields(all_fields,required_fields, submited_fields)
        submenu(form_files_paths, all_fields, required_fields, submited_fields, project_folder)
    elif option == "2":
        showContactFormFiles(form_files_paths)
        submenu(form_files_paths, all_fields, required_fields, submited_fields, project_folder)
    elif option == "3":
        showRandomFields()
        submenu(form_files_paths, all_fields, required_fields, submited_fields, project_folder)
    elif option == "4":
        generateEmail(all_fields, form_files_paths, project_folder)
        submenu(form_files_paths, all_fields, required_fields, submited_fields, project_folder)
    else:
        print("[red]Invalid option")
        exit()

def menu():
    project_folder = createProjectsFolder()
    form = getContactForm(project_folder)
    form_files_paths = formToFiles(form)
    all_fields = getRequiredFileds(form_files_paths)['all_fields']
    required_fields = getRequiredFileds(form_files_paths)['required_fields']
    submited_fields = getSubmitedFields(form_files_paths)
    random_fields = getRandomFields()
    checkRandomFields(all_fields, random_fields, submited_fields)
    submenu(form_files_paths, all_fields, required_fields, submited_fields, project_folder)
def contactForms():
    menu()
