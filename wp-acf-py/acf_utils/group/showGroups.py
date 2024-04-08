import json
from prettytable import PrettyTable
from termcolor import colored


def showGroups(file_path, show_fields=False):
    f = open(file_path,)
    data = json.load(f)
    for i in data:
        for j in i['fields']:
            if j['type'] == "group":
                print(colored(j['label'], 'blue'), colored(j['name'], 'green'))
                if show_fields:
                    for k in j['sub_fields']:
                        print(f'\t', colored(k['label'], 'blue'), colored(k['name'], 'green'), colored(k['type'], 'red'), colored(k['wrapper']['width'], 'yellow'), colored(k['key'], 'green'))
                        if k['type'] == "repeater":
                            for l in k['sub_fields']:
                                print(f'\t\t', colored(l['label'], 'blue'), colored(l['name'], 'green'), colored(l['type'], 'red'), colored(l['wrapper']['width'], 'yellow'), colored(l['key'], 'yellow'))

