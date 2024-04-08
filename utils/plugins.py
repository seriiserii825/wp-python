#!/usr/bin/python3
import os
import time

from termcolor import colored

from libs.select import selectMultiple

if not os.path.exists("front-page.php"):
    exit(colored("Please run this script from the root of your theme folder!", "red"))

plugins = [
        {"advanced-custom-fields-pro_6_0_6": "advanced-custom-fields-pro-6_0_6.zip"},
        {"advanced-custom-fields-pro-6_2_6_1": "advanced-custom-fields-pro-6_2_6_1.zip"},
        {"all-in-one-wp-migration": "all-in-one-wp-migration-7-79.zip"},
        {"classic-editor": False},
        {"tinymce-advanced": False},
        {"stops-core-theme-and-plugin-updates": False},
        {"safe-svg": False},
        {"contact-form-7": False},
        {"contact-form-7-honeypot": False},
        {"wp-mail-smtp": False},
        {"cookie-notice": False},
        {"wps-hide-login": False},
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
        {"3d-flipbook-dflip-lite": False},
        {"flow-flow-social-streams": False},
        {"add-to-any": False},
        {"woo-ajax-mini-cart": False},
        {"wp-smushit": False},
        ]


def listInstalledPlugins():
    os.system("wp plugin list")
    menu()

def getInstalledPlugins():
    installedPlugins = []
    os.chdir("../../plugins")
    for plugin in os.listdir():
        path = os.path.join(".", plugin)
        if os.path.isdir(path):
            installedPlugins.append(plugin)
    return installedPlugins

def installBasePlugins(plugins):
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
    exit()

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
    exit()

def menu():
    print(colored("1. List", "yellow"))
    print(colored("2. Install", "green"))
    print(colored("3. Uninstall", "blue"))
    print(colored("4. Exit", "red"))

    action = input("Choose action: ")
    if action == "1":
        listInstalledPlugins()
    elif action == "2":
        installBasePlugins(plugins)
    elif action == "3":
        uninstallPlugins(plugins)
    elif action == "4":
        exit()
    else:
        print("Wrong action!")

menu()
