import requests


def get_all_projects(url):
    projects = requests.get(url).json()
    for project in projects:
        print(f"Project name is {project['name']} \n project URL is {project['web_url']}")
