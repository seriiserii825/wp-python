#!/usr/bin/python3
import os
from termcolor import colored
from libs.select import selectMultiple

def pluginsFunc():
    base_plugins = [
            {"advanced-custom-fields-pro": "advanced-custom-fields-pro-6_0_6.zip"},
            {"all-in-one-wp-migration": "all-in-one-wp-migration-7-79.zip"},
            {"classic-editor": False},
            {"tinymce-advanced": False},
            {"stops-core-theme-and-plugin-updates": False},
            {"svg-support": False},
            {"wps-hide-login": False},
            {"wps-limit-login": False},
            ]

    plugins = [
            {"advanced-custom-fields-pro_6_0_6": "advanced-custom-fields-pro-6_0_6.zip"},
            {"advanced-custom-fields-pro-6_2_6_1": "advanced-custom-fields-pro-6_2_6_1.zip"},
            {"all-in-one-wp-migration": "all-in-one-wp-migration-7-79.zip"},
            {"admin-columns-pro": "admin-columns-pro-5.4.3.zip"},
            {"ac-addon-acf-2.6.4": "ac-addon-acf-2.6.4.zip"},
            {"classic-editor": False},
            {"tinymce-advanced": False},
            {"stops-core-theme-and-plugin-updates": False},
            {"safe-svg": False},
            {"contact-form-7": False},
            {"contact-form-7-honeypot": "contact-form-7-honeypot-2-1.zip"},
            {"wp-mail-smtp": False},
            {"cookie-notice": False},
            {"wps-hide-login": False},
            {"wps-limit-login": False},
            {"woocommerce-advanced-bulk-edit": "woocommerce-advanced-bulk-edit-5_2.zip"},
            {"seo-by-rank-math":"seo-by-rank-math.zip"},
            {"wp-pagenavi": False},
            {"error-log-monitor": False},
            {"wpglobus": "wpglobus.zip"},
            {"wpglobus-plus": "wpglobus-plus.zip"},
            {"query-monitor": False},
            {"post-duplicator": False},
            {"woocommerce": False},
            {"easy-woocommerce-auto-sku-generator": False},
            {"wc-fields-factory": False},
            {"advanced-bulk-edit": "advanced-bulk-edit-v1.3.zip"},
            {"webp-express": False},
            {"dearpdf-lite": "dearpdf-lite.zip"},
            {"3d-flipbook-dflip-lite": False},
            {"flow-flow-social-streams": False},
            {"add-to-any": False},
            {"woo-ajax-mini-cart": False},
            {"wp-smushit": False},
            ]


    def listInstalledPlugins():
        os.system("wp plugin list")

    def getInstalledPlugins():
        installedPlugins = []
        current_dir = os.getcwd()
        os.chdir("../../plugins")
        for plugin in os.listdir():
            path = os.path.join(".", plugin)
            if os.path.isdir(path):
                installedPlugins.append(plugin)
        os.chdir(current_dir)
        return installedPlugins

    def installBasePlugins(plugins):
        installed_plugins = getInstalledPlugins()
        print(installed_plugins)
        installed_plugins.sort()
        not_installed_plugins = []
        for plugin in plugins:
            for key, value in plugin.items():
                if key not in installed_plugins:
                    not_installed_plugins.append(plugin)

        if len(not_installed_plugins) == 0:
            print(colored("All plugins are installed!", "red"))
            exit()

        for plugin in not_installed_plugins:
            for key, value in plugin.items():
                print(f"Key: {key}, Value: {value}")
                if key in plugin:
                    print(f"Plugin {key} is already installed!")
                    if value == False:
                        os.system("wp plugin install " + key + " --activate")
                    else:
                        os.system("wp plugin install ~/Documents/plugins-wp/" + value + " --activate")

    def installPlugins(plugins):
        installed_plugins = getInstalledPlugins()
        installed_plugins.sort()
        not_installed_plugins = []
        for plugin in plugins:
            for key, value in plugin.items():
                if key not in installed_plugins:
                    not_installed_plugins.append(key)

        if len(not_installed_plugins) == 0:
            print(colored("All plugins are installed!", "red"))
            exit()

        not_installed_plugins.sort()
        selected_plugins = selectMultiple(not_installed_plugins)

        if len(selected_plugins) == 0:
            print(colored("No plugins selected!", "red"))
            exit()

        for plugin in plugins:
            for key, value in plugin.items():
                if key in selected_plugins:
                    if value == False:
                        os.system("wp plugin install " + key + " --activate")
                    else:
                        os.system("wp plugin install ~/Documents/plugins-wp/" + value + " --activate")

    def uninstallPlugins(plugins):
        installed_plugins = getInstalledPlugins()
        if len(installed_plugins) == 0:
            print(colored("No plugins installed!", "red"))
            exit()


        installed_plugins.sort()
        selected_plugins = selectMultiple(installed_plugins)
        for plugin in plugins:
            for key, value in plugin.items():
                if key in selected_plugins:
                    os.system("wp plugin deactivate " + key)
                    os.system("wp plugin uninstall " + key)

    def menu():
        print(colored("1. List", "yellow"))
        print(colored("2. Install Base Plugins", "green"))
        print(colored("3. Install Plugins", "green"))
        print(colored("4. Uninstall", "blue"))
        print(colored("5. Exit", "red"))

        action = input("Choose action: ")
        if action == "1":
            listInstalledPlugins()
            menu()
        elif action == "2":
            installBasePlugins(base_plugins)
            menu()
        elif action == "3":
            installPlugins(plugins)
            menu()
        elif action == "4":
            uninstallPlugins(plugins)
            menu()
        elif action == "5":
            exit()
        else:
            print("Wrong action!")

    menu()
