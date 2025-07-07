import os


def insertBeforeLastLine(file_path, content):
    # Open the file in read mode
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Insert a new line before the last line
        lines.insert(-1, content)
        # Open the file again in write mode
    with open(file_path, "w") as file:
        # Write all the lines back to the file
        file.writelines(lines)
    os.system(f"bat {file_path}")
