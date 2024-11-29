from termcolor import colored


def breadcrumbs(level_1, level_2 = '', level_3 ='', level_4 = '', level_5 = ''):
    print('----------------------------- Breadcrumbs -----------------------------')
    if level_1:
        print(colored(f"Breadcrumbs: {level_1} |", "blue"))
    if level_2:
        print(colored(f"Breadcrumbs: {level_1} | {level_2}", "green"))
    if level_3:
        print(colored(f"Breadcrumbs: {level_1} | {level_2} | {level_3}", "yellow"))
    if level_4:
        print(f"Breadcrumbs: {level_1} | {level_2} | {level_3} | {level_4}")
    if level_5:
        print(f"Breadcrumbs: {level_1} | {level_2} | {level_3} | {level_4} | {level_5}")
    print('----------------------------- Breadcrumbs -----------------------------')
