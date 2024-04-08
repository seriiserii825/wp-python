#!/usr/bin/python3
import pyperclip
from termcolor import colored
from libs.buffer import addToClipBoard

clipboard = pyperclip.paste()

if clipboard.startswith('git clone git@bitbucket.org:sites-bludelego'):
    print(colored(f'\nbitbucket url', 'green'))
    clipboard = clipboard.replace(clipboard, 'git clone git@bitbucket.org-b:sites-bludelego')
    print(colored(f'\n{clipboard}', 'blue'))
    addToClipBoard(clipboard)
else:
    print(colored(f'\nnot a bitbucket url', 'red'))

