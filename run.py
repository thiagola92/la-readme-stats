import os

from github import Github

from la_readme_stats.stars import count_user_repo_stars

github = Github(os.environ["ACCESS_TOKEN"])
user = github.get_user()

stats = {
    "name": user.name,
    "total_issues": user.get_issues(state="all").totalCount,
    "total_stars": count_user_repo_stars(user),
}


print(stats)
