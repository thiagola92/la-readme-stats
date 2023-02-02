import requests
from requests import Response

from la_readme_stats import ENDPOINT, HEADERS, LOGIN
from la_readme_stats.graphql import REPOS_QUERY, STATS_QUERY


def get_user_stats() -> dict:
    json = fetch_json()
    user = json["data"]["user"]
    name = user["name"]
    total_commits = calculate_total_commits(user)
    total_repositories = user["repositories"]["totalCount"]
    total_followers = user["followers"]["totalCount"]
    total_pull_requests = user["pullRequests"]["totalCount"]
    total_repo_contributed = user["repositoriesContributedTo"]["totalCount"]
    total_stars = calcualte_total_stars(user)
    total_issues = calculate_total_issues(user)

    while user["repositories"]["pageInfo"]["hasNextPage"]:
        after = user["repositories"]["pageInfo"]["endCursor"]
        json = fetch_json(after)
        user = json["data"]["user"]
        total_stars += calcualte_total_stars(user)

    return {
        "name": name,
        "total_commits": total_commits,
        "total_repositories": total_repositories,
        "total_followers": total_followers,
        "total_repo_contributed": total_repo_contributed,
        "total_stars": total_stars,
        "total_pull_requests": total_pull_requests,
        "total_issues": total_issues,
    }


def fetch_json(after: str = None) -> dict:
    variables = {"login": LOGIN}

    if not after:
        query = STATS_QUERY  # First request
    else:
        variables["after"] = after
        query = REPOS_QUERY

    response: Response = requests.post(
        ENDPOINT,
        headers=HEADERS,
        json={"query": query, "variables": variables},
    )

    response.raise_for_status()

    json = response.json()

    if json.get("errors"):
        raise Exception(str(json["errors"]))

    return json


def calculate_total_commits(user: dict) -> int:
    contributions = user["contributionsCollection"]
    total_commits = contributions["totalCommitContributions"]  # Normal commits
    total_commits += contributions["restrictedContributionsCount"]  # Private commits

    return total_commits


def calcualte_total_stars(user: dict) -> int:
    nodes = user["repositories"]["nodes"]
    total_stars = sum([n["stargazers"]["totalCount"] for n in nodes])

    return total_stars


def calculate_total_issues(user: dict) -> int:
    return user["openIssues"]["totalCount"] + user["closedIssues"]["totalCount"]
