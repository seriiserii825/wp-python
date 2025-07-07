from rich import print
from rich.panel import Panel


def checkHoneypot(form_files_paths):
    fields = []
    form_html = form_files_paths['html']
    items = []
    with open(form_html, "r") as f:
        line = f.read().strip()
        fields = line.split('[')
        for field in fields:
            if ']' in field:
                items.append(field.split(']')[0])
    #check for honeypot field if exists
    honeypot = [item for item in items if 'honeypot' in item]
    if honeypot:
        print(Panel(f"[green]Honeypot field found: {honeypot}"))
    else:
        print(Panel(f"[red]Honeypot field not found"))
