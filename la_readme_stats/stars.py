from github.AuthenticatedUser import AuthenticatedUser


def count_user_repo_stars(user: AuthenticatedUser):
    return sum(
        [
            repo.get_stargazers().totalCount
            for repo in user.get_repos(affiliation="owner", direction="asc")
        ]
    )
