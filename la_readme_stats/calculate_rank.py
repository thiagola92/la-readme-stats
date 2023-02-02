import math

COMMITS_OFFSET = 1.65
CONTRIBS_OFFSET = 1.65
ISSUES_OFFSET = 1
STARS_OFFSET = 0.75
PRS_OFFSET = 0.5
FOLLOWERS_OFFSET = 0.45
REPO_OFFSET = 1

ALL_OFFSETS = (
    CONTRIBS_OFFSET
    + ISSUES_OFFSET
    + STARS_OFFSET
    + PRS_OFFSET
    + FOLLOWERS_OFFSET
    + REPO_OFFSET
)

RANK_S_VALUE = 1
RANK_DOUBLE_A_VALUE = 25
RANK_A2_VALUE = 45
RANK_A3_VALUE = 60
RANK_B_VALUE = 100

TOTAL_VALUES = (
    RANK_S_VALUE + RANK_DOUBLE_A_VALUE + RANK_A2_VALUE + RANK_A3_VALUE + RANK_B_VALUE
)


def get_rank(stats):
    score = (
        stats["total_commits"] * COMMITS_OFFSET
        + stats["total_repo_contributed"] * CONTRIBS_OFFSET
        + stats["total_issues"] * ISSUES_OFFSET
        + stats["total_stars"] * STARS_OFFSET
        + stats["total_pull_requests"] * PRS_OFFSET
        + stats["total_followers"] * FOLLOWERS_OFFSET
        + stats["total_repositories"] * REPO_OFFSET
    ) / 100

    normalized_score = normalcdf(score) * 100

    if normalized_score < RANK_S_VALUE:
        return "S+"
    elif normalized_score < RANK_DOUBLE_A_VALUE:
        return "S"
    elif normalized_score < RANK_A2_VALUE:
        return "A++"
    elif normalized_score < RANK_A3_VALUE:
        return "A+"
    return "B+"


# https://stackoverflow.com/questions/5259421/cumulative-distribution-function-in-javascript/5263759#5263759
# https://github.com/anuraghazra/github-readme-stats/blob/master/src/calculateRank.js
def normalcdf(mean: float) -> float:
    sigma = TOTAL_VALUES
    to = ALL_OFFSETS

    z = (to - mean) / math.sqrt(2 * sigma * sigma)
    t = 1 / (1 + 0.3275911 * abs(z))
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    erf = 1 - ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t * math.exp(-z * z)
    sign = 1

    if z < 0:
        sign = -1

    return (1 / 2) * (1 + sign * erf)
