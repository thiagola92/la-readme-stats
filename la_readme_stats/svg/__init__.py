from pathlib import Path

ICON = {
    "commit": Path("la_readme_stats/svg/commit.svg").read_text(),
    "contribution": Path("la_readme_stats/svg/contribution.svg").read_text(),
    "star": Path("la_readme_stats/svg/star.svg").read_text(),
    "pull_request": Path("la_readme_stats/svg/pull_request.svg").read_text(),
    "issue": Path("la_readme_stats/svg/issue.svg").read_text(),
}

STATS = Path("la_readme_stats/html/stats.html").read_text()
