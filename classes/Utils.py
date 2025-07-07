import re


class Utils:
    @staticmethod
    def camelToKebabCase(s):
        return re.sub(r'(?<!^)(?=[A-Z])', '-', s).lower()

