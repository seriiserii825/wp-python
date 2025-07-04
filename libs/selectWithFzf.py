from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()


def selectWithFzf(items):
    selected_item = fzf.prompt(items)
    return selected_item[0]
