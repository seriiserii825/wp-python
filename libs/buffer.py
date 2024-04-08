import os

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| xclip -selection clipboard'
    os.system(command)

def addToClipBoardFile(file):
    command = f"cat {file} | xclip -selection clipboard"
    # print(command)
    os.system(command)

def getFromClipBoard():
    command = 'xclip -o -selection clipboard'
    return os.popen(command).read().strip()
