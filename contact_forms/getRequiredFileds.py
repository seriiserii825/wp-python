def getRequiredFileds(form_files_paths):
    fields = []
    ignored_fields = ['timecheck_enabled', 'honeypot', 'acceptance', 'submit']
    form_html = form_files_paths['html']
    items = []
    with open(form_html, "r") as f:
        line = f.read().strip()
        fields = line.split('[')
        for field in fields:
            if ']' in field:
                items.append(field.split(']')[0])
    # Remove elements from 'over_fields' that contain any of the ignored fields
    required_fields = [item for item in items if '*' in item ]
    required_fields = [item.split(' ')[1] for item in required_fields]
    items = [field for field in items if not any(ignored_field in field for ignored_field in ignored_fields)]
    items = [item.split(' ')[1] for item in items]
    return {
            'all_fields': items,
            'required_fields': required_fields
            }

