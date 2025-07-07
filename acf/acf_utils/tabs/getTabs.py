import json


def getTabs(file_path):
    tabs = []
    f = open(
        file_path,
    )
    data = json.load(f)
    for i in data:
        for j in i["fields"]:
            if j["type"] == "tab":
                tab = {
                    "name": j["name"],
                    "label": j["label"],
                    "index": i["fields"].index(j),
                }
                tabs.append(tab)
    return tabs
