from acf.acf_utils.fields.getFieldId import getFieldId


def newTab(title):
    field_id = getFieldId()
    tab = {}
    tab["key"] = field_id
    tab["label"] = title
    tab["name"] = ""
    tab["aria-label"] = ""
    tab["type"] = "tab"
    tab["instructions"] = ""
    tab["required"] = 0
    tab["conditional_logic"] = 0
    tab["wrapper"] = {"width": "", "class": "", "id": ""}
    tab["placement"] = "top"
    tab["endpoint"] = 0
    return tab
