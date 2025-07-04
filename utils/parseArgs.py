import argparse


def parseArgs(arg_name, callBack, menu):
    parser = argparse.ArgumentParser(description="Example of flag and value parsing")
    parser.add_argument("--menu", type=str, help="Menu item")
    args = parser.parse_args()

    if args.menu:
        if args.menu == arg_name:
            callBack()
    else:
        menu()
