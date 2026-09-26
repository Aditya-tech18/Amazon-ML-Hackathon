FEATURE_COLUMNS = [
    "name_exact",
    "name_normalized_exact",
    "name_token_jaccard",
    "name_char_similarity",
    "name_length_ratio",

    "address_exact",
    "address_normalized_exact",
    "address_token_jaccard",
    "address_char_similarity",
    "address_numeric_overlap",
    "address_left_missing",
    "address_right_missing",

    "country_match",
    "country_left_missing",
    "country_right_missing",

    "name_address_agreement",
    "name_country_agreement",
    "address_country_agreement",
]

TARGET_COLUMN = "label"

ID_COLUMNS = [
    "s1_id",
    "candidate_id",
]

RANDOM_STATE = 42
