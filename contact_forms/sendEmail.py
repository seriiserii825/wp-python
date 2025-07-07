import os


def sendEmail(form_files_paths):
    command = (
        f"mutt -s 'Subject here' seriiburduja@gmail.com < {form_files_paths['mail']}"
    )
    os.system(command)
    # echo "Email body text" | mutt -s "Subject here" seriiburduja@gmail.com
