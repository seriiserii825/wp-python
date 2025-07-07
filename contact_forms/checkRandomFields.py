from rich import print


def checkRandomFields(all_fields, random_fields, submited_fields):
    random_fields_names = [field["name"] for field in random_fields]
    submited_fields.sort()
    random_fields_names.sort()
    all_fields.sort()
    # get difference between all_fields and random_fields
    all_fields_random = set(all_fields) - set(random_fields_names)
    # get difference between all_fields and submited_fields
    all_fields_submited = set(all_fields) - set(submited_fields)
    # get difference between submited_fields and all_fields
    submited_fields_all = set(submited_fields) - set(all_fields)

    if len(all_fields_random) > 0:
        print("[red] Html fields not in random")
        [print(f"[red]{field}") for field in all_fields_random]
        return False
    elif len(all_fields_submited) > 0:
        print("[red] Html fields not in submited")
        [print(f"[red]{field}") for field in all_fields_submited]
        return False
    elif len(submited_fields_all) > 0:
        print("[red] Submited fields not in html")
        [print(f"[red]{field}") for field in submited_fields_all]
        return False
    else:
        return True
