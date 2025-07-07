import json
import os


def getWpPages():
    json_pages = os.popen("wp post list --post_type=page --format=json").read()
    data = json.loads(json_pages)
    pages = []
    for page in data:
        page_name = page
        pages.append(page_name)
    return pages
