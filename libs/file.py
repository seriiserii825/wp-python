from rich import print
def writeToFile(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
    print(f'[green]File {file_path} was written successfully')


