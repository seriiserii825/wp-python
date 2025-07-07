import os

from pyfzf.pyfzf import FzfPrompt


def showAllTaxonomies():
    os.system("wp taxonomy list")

def showTaxonomy(tax):
    os.system(f"wp term list {tax}")

def taxonomies():
# main manu
    menu_items = [
        "Show all",
        "Clear all",
    ]

    fzf = FzfPrompt()
    menu_entry = fzf.prompt(menu_items)

    if menu_entry[0] == "Show all":
        showAllTaxonomies()
    elif menu_entry[0] == "Clear all":
        showAllTaxonomies()
        tax = input("Enter the taxonomy to clear: ")
        all_terms = os.popen(f"wp term list {tax} --field=term_id").read().strip().split("\n")
        for term_id in all_terms:
            os.system(f"wp term delete {tax} {term_id}")
        showTaxonomy(tax)
