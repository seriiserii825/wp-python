#!/usr/bin/python3
import os

def filesSpaceToUnderscores():
    for filename in os.listdir("."):
        new_file = filename.replace(' ', '-')
        os.replace(filename, new_file)

filesSpaceToUnderscores()

languages = [ {"Ё": "YO"}, {"Й": "I"}, {"Ц": "TS"}, {"У": "U"}, {"К": "K"}, {"Е": "E"}, {"Н": "N"}, {"Г": "G"}, {"Ш": "SH"}, {"Щ": "SCH"}, {"З": "Z"}, {"Х": "H"}, {"Ъ": "I"}, {"ё": "yo"}, {"й": "i"}, {"ц": "ts"}, {"у": "u"}, {"к": "k"}, {"е": "e"}, {"н": "n"}, {"г": "g"}, {"ш": "sh"}, {"щ": "sch"}, {"з": "z"}, {"х": "h"}, {"ъ": "i"}, {"Ф": "F"}, {"Ы": "I"}, {"В": "V"}, {"А": "A"}, {"П": "P"}, {"Р": "R"}, {"О": "O"}, {"Л": "L"}, {"Д": "D"}, {"Ж": "ZH"}, {"Э": "E"}, {"ф": "f"}, {"ы": "i"}, {"в": "v"}, {"а": "a"}, {"п": "p"}, {"р": "r"}, {"о": "o"}, {"л": "l"}, {"д": "d"}, {"ж": "zh"}, {"э": "e"}, {"Я": "Ya"}, {"Ч": "CH"}, {"С": "S"}, {"М": "M"}, {"И": "I"}, {"Т": "T"}, {"Ь": "I"}, {"Б": "B"}, {"Ю": "YU"}, {"я": "ya"}, {"ч": "ch"}, {"с": "s"}, {"м": "m"}, {"и": "i"}, {"т": "t"}, {"ь": "i"}, {"б": "b"}, {"ю": "yu"} ]

def transliterate():
    for filename in os.listdir("."):
        new_file = filename
        for letter in filename:
            for item in languages:
                for index, key in item.items():
                    if index == letter:
                        new_file = new_file.replace(letter, key)
        os.replace(filename, new_file)
transliterate()
