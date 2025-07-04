import subprocess

from rich import print


def runCommand(command_list, silent=False):
    """
    Run a shell command with subprocess.run, and check for errors.

    Args:
        command_list (list): Command and arguments as a list.
        silent (bool): If True, suppress output.

    Returns:
        bool: True if the command succeeded, False otherwise.
    """
    try:
        subprocess.run(
            command_list,
            check=True,
            stdout=subprocess.PIPE if silent else None,
            stderr=subprocess.PIPE if silent else None,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(
            f"[red]Error: Command '{' '.join(command_list)}' \
                    failed with code {e.returncode}"
        )
        if silent:
            print("[red][stderr]:", e.stderr.strip())
        exit(1)
