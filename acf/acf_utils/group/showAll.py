import json
from prettytable import PrettyTable
from termcolor import colored


def showAll(file_path, group_index=None):
    f = open(file_path,)
    data = json.load(f)

    if group_index:
        group = data[0]['fields'][group_index]
        group_subfields = data[0]['fields'][group_index]['sub_fields']
        print(colored(group['label'], 'blue'), colored(group['name'], 'green'), colored(group['type'], 'red'), colored((group['layout']), 'yellow'))
        for k in group_subfields:
            print(f'\t', colored(k['label'], 'blue'), colored(k['name'], 'green'), colored(k['type'], 'red'), colored(k['wrapper']['width'], 'yellow'), colored(k['key'], 'green'))
            if k['type'] == "repeater":
                for l in k['sub_fields']:
                    print(f'\t\t', colored(l['label'], 'blue'), colored(l['name'], 'green'), colored(l['type'], 'red'), colored(l['wrapper']['width'], 'yellow'), colored(l['key'], 'yellow'))
            else:
                continue
    else:
        for i in data:
            for j in i['fields']:
                if j['type'] == "group":
                    print(colored(j['label'], 'blue'), colored(j['name'], 'green'), colored(j['type'], 'red'), colored((j['layout']), 'yellow'))
                else:
                    print(colored(j['label'], 'blue'), colored(j['name'], 'green'), colored(j['type'], 'red'))
                if j['type'] == "group":
                    for k in j['sub_fields']:
                        print(f'\t', colored(k['label'], 'blue'), colored(k['name'], 'green'), colored(k['type'], 'red'), colored(k['wrapper']['width'], 'yellow'), colored(k['key'], 'green'))
                        if k['type'] == "repeater":
                            for l in k['sub_fields']:
                                print(f'\t\t', colored(l['label'], 'blue'), colored(l['name'], 'green'), colored(l['type'], 'red'), colored(l['wrapper']['width'], 'yellow'), colored(l['key'], 'yellow'))

