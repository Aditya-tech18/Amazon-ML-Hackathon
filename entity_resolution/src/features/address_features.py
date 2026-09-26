from rapidfuzz import fuzz

from entity_resolution.src.features.normalization import (
    normalize_text,
    normalize_for_comparison,
    tokenize,
    extract_numeric_tokens,
)


def exact_match(left, right):
    if not left or not right:
        return 0.0

    return float(
        str(left).strip().casefold()
        == str(right).strip().casefold()
    )


def normalized_exact_match(left, right):
    left_norm = normalize_text(left)
    right_norm = normalize_text(right)

    if not left_norm or not right_norm:
        return 0.0

    return float(left_norm == right_norm)


def token_jaccard(left, right):
    left_tokens = tokenize(left)
    right_tokens = tokenize(right)

    if not left_tokens or not right_tokens:
        return 0.0

    union = left_tokens | right_tokens

    if not union:
        return 0.0

    return len(left_tokens & right_tokens) / len(union)


def character_similarity(left, right):
    left_norm = normalize_for_comparison(left)
    right_norm = normalize_for_comparison(right)

    if not left_norm or not right_norm:
        return 0.0

    return fuzz.ratio(left_norm, right_norm) / 100.0


def numeric_token_overlap(left, right):
    """
    Compare numbers appearing in addresses.

    Useful for house numbers, plot numbers,
    postal codes, route numbers, etc.
    """

    left_numbers = extract_numeric_tokens(left)
    right_numbers = extract_numeric_tokens(right)

    if not left_numbers or not right_numbers:
        return 0.0

    intersection = left_numbers & right_numbers
    union = left_numbers | right_numbers

    if not union:
        return 0.0

    return len(intersection) / len(union)


def address_missing(value):
    if value is None:
        return 1.0

    if not isinstance(value, str):
        value = str(value)

    return float(not value.strip())


def address_features(left, right):
    """
    Compute address-based features for one candidate pair.
    """

    return {
        "address_exact": exact_match(left, right),

        "address_normalized_exact": normalized_exact_match(
            left, right
        ),

        "address_token_jaccard": token_jaccard(
            left, right
        ),

        "address_char_similarity": character_similarity(
            left, right
        ),

        "address_numeric_overlap": numeric_token_overlap(
            left, right
        ),

        "address_left_missing": address_missing(left),

        "address_right_missing": address_missing(right),
    }
