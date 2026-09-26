def normalize_country(value):
    if value is None:
        return ""

    if not isinstance(value, str):
        value = str(value)

    return value.strip().casefold()


def country_match(left, right):
    left = normalize_country(left)
    right = normalize_country(right)

    if not left or not right:
        return 0.0

    return float(left == right)


def country_features(left, right):
    return {
        "country_match": country_match(left, right),
        "country_left_missing": float(
            not normalize_country(left)
        ),
        "country_right_missing": float(
            not normalize_country(right)
        ),
    }
