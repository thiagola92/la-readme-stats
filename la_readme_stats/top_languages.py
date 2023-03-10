from collections import Counter

import requests
from requests import Response

from la_readme_stats import ENDPOINT, HEADERS, LOGIN
from la_readme_stats.graphql import LANGUAGES_QUERY


def get_top_languages() -> dict:
    json = fetch_json()
    nodes = json["data"]["user"]["repositories"]["nodes"]
    nodes = [n for n in nodes if len(n["languages"]["edges"]) > 0]

    return calculate_top_languages(nodes)


def fetch_json() -> dict:
    response: Response = requests.post(
        ENDPOINT,
        headers=HEADERS,
        json={"query": LANGUAGES_QUERY, "variables": {"login": LOGIN}},
    )

    response.raise_for_status()

    json = response.json()

    if json.get("errors"):
        raise Exception(str(json["errors"]))

    return json


def calculate_top_languages(nodes: list) -> list:
    counter = Counter({})
    colors = {}

    for node in nodes:
        for language in node["languages"]["edges"]:
            name = language["node"]["name"]
            colors[name] = language["node"]["color"]
            counter += Counter({name: language["size"]})

    total_count = counter.total()
    top_languages = [
        get_language_details(name, size, total_count, colors)
        for name, size in counter.most_common(5)
    ]

    return top_languages


def get_language_details(name: str, size: int, total_count: int, colors: dict) -> dict:
    return {
        "name": name,
        "size": round((size / total_count) * 100, 2),
        "color": colors[name],
    }
