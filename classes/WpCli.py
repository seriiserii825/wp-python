import os
import subprocess
class WpCli():
    def runWp(self, command: str):
        os.system(f"HOST_UID=$(id -u) HOST_GID=$(id -g) docker-compose run --rm wpcli {command}")
        # command_arr = command.split(" ")
        # full_cmd = ["docker-compose", "run", "--rm", "wpcli"] + command_arr
        #
        # print(f"Running command: {' '.join(full_cmd)}")
        #
        # process = subprocess.Popen(
        #     full_cmd,
        #     stdout=subprocess.PIPE,
        #     stderr=subprocess.STDOUT,
        #     universal_newlines=True,
        #     bufsize=1
        # )
        #
        # # Print output in real-time
        # for line in process.stdout:
        #     print(line, end="")
        #
        # process.wait()
        # print(f"Exit code: {process.returncode}")
