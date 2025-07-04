import os

import plyer
import pyperclip


def addToClipBoard(text):
    pyperclip.copy(text.strip())
    plyer.notification.notify(
        title="Buffer", message=text, app_name="Buffer", timeout=5
    )


def addToClipBoardFile(file):
    command = f"cat {file} | xclip -selection clipboard"
    print(command)
    os.system(command)


def getFromClipBoard():
    command = "xclip -o -selection clipboard"
    print(f"command from buffer: {command}")
    return os.popen(command).read().strip()
