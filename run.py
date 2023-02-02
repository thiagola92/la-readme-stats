from la_readme_stats.calculate_rank import get_rank
from la_readme_stats.top_languages import get_top_languages
from la_readme_stats.user_stats import get_user_stats

top_languages = get_top_languages()
user_stats = get_user_stats()
rank = get_rank(user_stats)

print(top_languages)
print(user_stats)
print(rank)
