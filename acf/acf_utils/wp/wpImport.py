from classes.WpCli import WpCli

def wpImport():
    wp_cli = WpCli()
    wp_cli.runWp("acf clean")
    wp_cli.runWp("acf import --all")

