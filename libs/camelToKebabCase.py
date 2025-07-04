import re


def camelToKebabCase(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", s).lower()
