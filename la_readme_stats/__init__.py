import os

ENDPOINT = "https://api.github.com/graphql"
HEADERS = {"Authorization": f"bearer {os.environ['TOKEN']}"}
LOGIN = os.environ["LOGIN"]
