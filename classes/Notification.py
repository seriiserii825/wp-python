import os


class Notification:
    @staticmethod
    def notify(title: str = "", message: str = ""):
        os.system(f'notify-send "{title}" "{message}"')
