import os

from pick import pick
from backups.listBackup import listBackup


def restoreBackup():
    listBackup()
    os.chdir("../../ai1wm-backups")
    backup_files = os.listdir()
    title = 'Select plugins'
    backups_array = []
    selected_plugins = []
    for file in backup_files:
        if file.endswith('.wpress'):
            backups_array.append(file)
    selected = pick(backups_array, title, multiselect=False, min_selection_count=1)
    print(selected)
    for item in selected:
        selected_plugins.append(item)
    os.system(f"wp ai1wm restore {selected_plugins[0]}")

