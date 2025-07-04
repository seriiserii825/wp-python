import os

from termcolor import colored


def checkPiniaLayout(layout_path):
    if not os.path.exists(layout_path):
        print(colored("Creating pinia layout file...", "green"))
        with open(layout_path, "w") as f:
            layout_code = """
                import { ref } from "vue";
                import { defineStore } from "pinia";
                export const useDefaultStore = defineStore("default", () => {
                  return {
                  };
                });
            """
            f.write(layout_code)
    else:
        print(colored("Layout pinia exists", "blue"))
