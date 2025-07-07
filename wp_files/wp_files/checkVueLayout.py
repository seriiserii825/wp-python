import os

from termcolor import colored


def checkVueLayout(layout_path):
    if not os.path.exists(layout_path):
        print(colored("Creating vue layout file...", "green"))
        with open(layout_path, 'w') as f:
            layout_code = """
              <script lang="ts" setup>

              </script>
              <template>
              <div class="vue"></div>
              </template>
              <style lang="scss">
              
              </style>
            """
            f.write(layout_code)
    else:
        print(colored("Layout vue exists", "blue"))
