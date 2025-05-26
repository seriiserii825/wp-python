def getSubmitedFields(form_files_paths):
    form_mail = form_files_paths['mail']
    fields = []
    with open(form_mail, "r") as f:
        line = f.read().strip()
        fields = line.split('[')
        items = []
        response = []
        for field in fields:
            if ']' in field:
                items.append(field.split(']')[0])
        for item in items:
            if not item.startswith('_'):
                response.append(item)
    return response

