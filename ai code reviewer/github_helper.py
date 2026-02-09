from github import Github
import base64
import os

def get_repo_files(repo_url):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)

    repo_name = repo_url.replace("https://github.com/", "")
    repo = g.get_repo(repo_name)

    files = []
    contents = repo.get_contents("")

    while contents:
        file = contents.pop(0)

        if file.type == "dir":
            contents.extend(repo.get_contents(file.path))
        else:
            if file.path.endswith((".py",".js",".java",".cpp",".c",".ts")):
                files.append(file.path)

    return files


def get_file_content(repo_url, filepath):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)

    repo_name = repo_url.replace("https://github.com/", "")
    repo = g.get_repo(repo_name)

    file = repo.get_contents(filepath)

    return base64.b64decode(file.content).decode("utf-8")
