import os

from pick import pick

from libs.orderFiles import orderFiles


def restoreFromDownloads():
    downloads_dir = os.path.expanduser("~/Downloads")
    backup_files = orderFiles(downloads_dir)
    title = 'Select files'
    backups_array = []
    selected_plugins = []
    for file in backup_files:
        if file.endswith('.wpress'):
            backups_array.append(file)
    selected = pick(backups_array, title, multiselect=False, min_selection_count=1)
    for item in selected:
        selected_plugins.append(item)
    os.system(f"cp ~/Downloads/{selected_plugins[0]} ../../ai1wm-backups")
    print(f"Selected file: {selected_plugins[0]}")
    os.system(f"wp ai1wm restore {selected_plugins[0]}")

