from pathlib import Path

from la_readme_stats.svg import ICON, STATS


def draw_user_stats(stats: dict):
    page = STATS.replace("{name}", stats["name"]).replace("{rank}", stats["rank"])

    icon_label_value = [
        (ICON["star"], "Total Stars Earned", stats["total_stars"]),
        (ICON["commit"], "Total Commits", stats["total_commits"]),
        (ICON["pull_request"], "Total PRs", stats["total_pull_requests"]),
        (ICON["issue"], "Total Issues", stats["total_issues"]),
        (ICON["contribution"], "Contributed to", stats["total_repo_contributed"]),
    ]

    line = 0

    for icon, label, value in icon_label_value:
        page = (
            page.replace("{translate}", str(line), 1)
            .replace("{icon}", icon, 1)
            .replace("{label}", label, 1)
            .replace("{value}", str(value), 1)
        )
        line += 25

    Path("la_readme_stats/output/stats.svg").write_text(page)
