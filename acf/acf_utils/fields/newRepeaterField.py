from acf_utils.fields.getFieldId import getFieldId


def newRepeaterField(field_name, field_slug, field_type, field_width):
    field_id = getFieldId()
    field = {}
    field["key"] = field_id
    field["label"] = field_name
    field["name"] = field_slug
    field["aria-label"] = ""
    field["type"] = field_type
    field["instructions"] = ""
    field["required"] = 0
    field["conditional_logic"] = 0
    field["wrapper"] = {"width": field_width, "class": "", "id": ""}
    field["default_value"] = ""
    field["maxlength"] = ""
    field["placeholder"] = ""
    field["prepend"] = ""
    field["append"] = ""

    if field_type == "wysiwyg":
        field["toolbar"] = "basic"
        field["media_upload"] = 0
    if field_type == "image" or field_type == "gallery" or field_type == "file":
        field["return_format"] = "url"
    if field_type == "repeater":
        field["layout"] = "table"
        field["button_label"] = "Add Row"
        field["sub_fields"] = []
    return field
