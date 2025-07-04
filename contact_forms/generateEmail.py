import os
import random

from rich import print

from contact_forms.getRandomFields import getRandomFields
from contact_forms.sendEmail import sendEmail


def generateEmail(all_fields, form_files_paths, project_folder):
    form_mail_path = form_files_paths["mail"]
    choice = input("Do you want to generate random data or set fields?(r/s)")
    random_fields = getRandomFields()

    if choice == "r":
        with open(form_mail_path, "r") as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                for field in all_fields:
                    if field in line:
                        random_field = [
                            random_item
                            for random_item in random_fields
                            if random_item["name"] == field
                        ]
                        if len(random_field) > 0:
                            lines[index] = lines[index].replace(
                                f"[{field}]", random.choice(random_field[0]["value"])
                            )
        with open(form_mail_path, "w") as f:
            f.writelines(lines)

        os.system(f"bat {form_mail_path}")
        send_email = input("[green]Do you want to send email?(y/n)")
        if send_email == "y":
            sendEmail(form_files_paths)
            os.system(f"rm -rf {project_folder}")
        else:
            return
    elif choice == "s":
        print("Setting fields")
