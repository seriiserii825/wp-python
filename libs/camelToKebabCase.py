
import re


def camelToKebabCase(s):
    # Use regular expression to find capital letters preceded by a lowercase letter,
    # and insert a hyphen before each capital letter.
    return re.sub(r'(?<!^)(?=[A-Z])', '-', s).lower()
