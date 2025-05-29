import os
from rich import print
from classes.FilesHandle import FilesHandle
from data.base_plugins import base_plugins
from data.plugins import plugins
import subprocess


class Plugin():
    def __init__(self):
        self.base_plugins = base_plugins
        self.plugins = plugins
        self.abs_path_plugins = os.path.abspath("../../plugins")
        self.installed_plugins = self.getInstalledPlugins()
        self.not_installed_plugins = self.getNotInstalledPlugins(self.plugins)
        self.not_installed_base_plugins = self.getNotInstalledPlugins(
            self.base_plugins)

    def runWp(self, command: str):
        command_arr = command.split(" ")
        result = subprocess.run(
            ["docker-compose", "run", "--rm", "wpcli"] + command_arr,
            capture_output=True,
            text=True
        )
        print(result.stdout)

    def listInstalledPlugins(self):
        self.runWp("plugin list --format=csv")

    def getInstalledPlugins(self):
        installedPlugins = []
        current_dir = os.getcwd()
        os.chdir(self.abs_path_plugins)
        for plugin in os.listdir():
            path = os.path.join(".", plugin)
            if os.path.isdir(path):
                installedPlugins.append(plugin)
        os.chdir(current_dir)
        return installedPlugins

    def getNotInstalledPlugins(self, plugins: list):
        self.installed_plugins.sort()
        not_installed_plugins = []
        for plugin in plugins:
            for key, _ in plugin.items():
                if key not in self.installed_plugins:
                    not_installed_plugins.append(plugin)

        if len(not_installed_plugins) == 0:
            return []
        else:
            return not_installed_plugins

    def haveUninstalledPlugins(self):
        if len(self.not_installed_plugins) == 0:
            print("[red]All base plugins are installed!")
            exit()

    def installPlugins(self, plugins: list):
        for plugin in plugins:
            for key, value in plugin.items():
                print(f"Key: {key}, Value: {value}")
                if key in plugin:
                    if value == False:
                        self.runWp("plugin install " + key + " --activate")
                    else:
                        os.system(
                            f"{self.wp} plugin install ~/Documents/plugins-wp/" + value + " --activate")
                        self.runWp("plugin install ~/Documents/plugins-wp/" + value + " --activate")

    def installBasePlugins(self):
        self.haveUninstalledPlugins()
        self.installPlugins(self.base_plugins)

    def installOtherPlugins(self):
        self.haveUninstalledPlugins()
        current_dir = os.getcwd()
        fh = FilesHandle(current_dir)
        plugins = self.pluginsToStrList(self.not_installed_plugins)
        selected_plugins = fh.selectMultiple(plugins)

        if len(selected_plugins) == 0:
            print("[red]No plugins selected!")
            exit()

        plugins = self.pluginsFromStrListToDict(selected_plugins)
        self.installPlugins(plugins)

    def pluginsToStrList(self, plugins: list):
        plugins_str_list = []
        for plugin in plugins:
            for key, _ in plugin.items():
                plugins_str_list.append(key)
        return plugins_str_list

    def pluginsFromStrListToDict(self, plugins: list):
        plugins_dict = []
        for plugin in plugins:
            for item in self.not_installed_plugins:
                for key, _ in item.items():
                    if key == plugin:
                        plugins_dict.append(item)
        return plugins_dict

    def uninstallPlugins(self):
        self.installed_plugins.sort()
        fh = FilesHandle(os.getcwd())
        selected_plugins = fh.selectMultiple(self.installed_plugins)
        for plugin in plugins:
            for key, _ in plugin.items():
                if key in selected_plugins:
                    self.runWp("plugin deactivate " + key)
                    self.runWp("plugin uninstall " + key)
