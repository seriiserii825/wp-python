import os

from libs.selectWithFzf import selectWithFzf


def chooseDir(basepath):
    choosed_dir = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                choosed_dir.append(entry.name)
    choosed_dir.sort()
    selected_dir = selectWithFzf(choosed_dir)
    return selected_dir
