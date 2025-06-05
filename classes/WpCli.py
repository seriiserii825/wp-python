import os
class WpCli():
    def runWp(self, command: str):
        os.system(f"HOST_UID=$(id -u) HOST_GID=$(id -g) docker-compose run --rm wpcli {command}")
