RANK_S_VALUE = 1
RANK_DOUBLE_A_VALUE = 25
RANK_A2_VALUE = 45
RANK_A3_VALUE = 60
RANK_B_VALUE = 100
TOTAL_VALUES = (
    RANK_S_VALUE + RANK_DOUBLE_A_VALUE + RANK_A2_VALUE + RANK_A3_VALUE + RANK_B_VALUE
)


def get_level(normalized_score):
    if normalized_score < RANK_S_VALUE:
        return "S+"
    elif normalized_score < RANK_S_VALUE:
        return "S"
    elif normalized_score < RANK_S_VALUE:
        return "A++"
    elif normalized_score < RANK_S_VALUE:
        return "A+"
    return "B+"
