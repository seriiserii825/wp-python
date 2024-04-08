import os
import subprocess
from libs.buffer import addToClipBoardFile

def convertFontsFunc():
    def checkInstalledApps():
        retval = subprocess.call(["which", "woff2_compress"])
        if retval != 0:
            print("Packagename not installed!")
            subprocess.call(["sudo", "apt", "install", "woff2", "-y"])

        retval = os.system("npm ls -g | grep ttf2woff")
        if retval != 0:
            print("Packagename not installed!")
            os.system("npm install -g ttf2woff")

    checkInstalledApps()

    def ttfToWoff2():
        for file in os.listdir("."):
            if file.endswith(".ttf"):
                subprocess.call(["ttf2woff", file, file.replace(".ttf", ".woff")])
                subprocess.call(["woff2_compress", file])
                os.remove(file)

    ttfToWoff2()

    def woffToCss():
        woff_files = [f for f in os.listdir(".") if f.endswith(".woff")]
        woff2_files = [f for f in os.listdir(".") if f.endswith(".woff2")]
        # create file fonts.css
        f = open("fonts.css", "w")
        rel_path = input("Enter relative path to fonts folder (default: assets/fonts): ")
        if rel_path == "":
            rel_path = "assets/fonts"
        for file in woff_files:
            file_name_without_extension = file.replace(".woff", "")
            file_name_without_extension_lower = file_name_without_extension.lower()
            font_style = "normal"
            font_weight = "normal"
            print(file_name_without_extension_lower)

            if "italic" in file_name_without_extension_lower:
                font_style = "italic"

            if "extralight" in file_name_without_extension_lower:
                font_weight = "200"
            elif "light" in file_name_without_extension_lower:
                font_weight = "300"
            if "extrabold" in file_name_without_extension_lower:
                font_weight = "800"
            elif "bold" in file_name_without_extension_lower:
                font_weight = "700"
            if "thin" in file_name_without_extension_lower:
                font_weight = "100"
            if "medium" in file_name_without_extension_lower:
                font_weight = "500"
            if "semibold" in file_name_without_extension_lower or "demibold" in file_name_without_extension_lower:
                font_weight = "600"
            if "black" in file_name_without_extension_lower or "heavy" in file_name_without_extension_lower:
                font_weight = "900"

            font_name = file_name_without_extension
            capital_name = font_name.capitalize()
            capital_name = capital_name.split('-')[0]
            code_block = f"""
            @font-face {{
               font-family: '{capital_name}'; 
               src: url('{rel_path}/{font_name}.woff2') format('woff2'),
               url('{rel_path}/{font_name}.woff') format('woff');
               font-weight: {font_weight};
               font-style: {font_style};
               font-display: swap;
             }}
            """
        
            f.write(code_block)
        f.close()
    woffToCss()
    addToClipBoardFile('fonts.css')
    command="rm fonts.css"
    os.system(command)
