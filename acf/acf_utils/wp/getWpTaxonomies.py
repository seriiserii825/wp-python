import json
import os


def getWpTaxonomies():
    json_taxonomies = os.popen("wp taxonomy list --fields=name --format=json").read()
    data = json.loads(json_taxonomies)
    taxonomies = []
    for taxonomy in data:
        taxonomy_name = taxonomy["name"]
        taxonomies.append(taxonomy_name)
    return taxonomies
