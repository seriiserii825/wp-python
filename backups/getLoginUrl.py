from utils.getProjects import getProjects


def getLoginUrl(theme_name, second_param = True):
    project = getProjects(theme_name)
    project_url = project['url']
    if second_param:
        return f"{project_url}/wp-admin"
    else:
        if not 'gestione' in project:
            return f"{project_url}/gestione"
        else:
            return f"{project_url}/{project['gestione']}"
