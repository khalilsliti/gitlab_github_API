import gitlab
import github
gitlab_username=input('Give the Gitlab username\n')
github_username=input('Give the Gitlab username\n')
print(f"The gitlab projects for the user {gitlab_username} are : \n ")
gitlab.get_all_projects(f"https://gitlab.com/api/v4/users/{gitlab_username}/projects");
print("****************************************************************************** \n")
print(f"The github projects for the user {gitlab_username} are \n : ")
github.get_all_projects(f"https://api.github.com/users/{github_username}/repos");