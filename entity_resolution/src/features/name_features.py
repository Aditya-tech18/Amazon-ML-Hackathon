from rapidfuzz import fuzz

from entity_resolution.src.features.normalization import (
    normalize_text,
    normalize_for_comparison,
    tokenize,
)


def exact_match(left, right):
    """
    Raw-string exact match.
    """
    if not left or not right:
        return 0.0

    return float(
        str(left).strip().casefold()
        == str(right).strip().casefold()
    )


def normalized_exact_match(left, right):
    """
    Exact match after normalization.
    """
    left_norm = normalize_text(left)
    right_norm = normalize_text(right)

    if not left_norm or not right_norm:
        return 0.0

    return float(left_norm == right_norm)


def token_jaccard(left, right):
    """
    Jaccard similarity between normalized token sets.

    J(A,B) = |A ∩ B| / |A ∪ B|
    """
    left_tokens = tokenize(left)
    right_tokens = tokenize(right)

    if not left_tokens or not right_tokens:
        return 0.0

    union = left_tokens | right_tokens

    if not union:
        return 0.0

    return len(left_tokens & right_tokens) / len(union)


def character_similarity(left, right):
    """
    Character-level similarity using RapidFuzz.
    Returns a value between 0 and 1.
    """
    left_norm = normalize_for_comparison(left)
    right_norm = normalize_for_comparison(right)

    if not left_norm or not right_norm:
        return 0.0

    return fuzz.ratio(left_norm, right_norm) / 100.0


def length_ratio(left, right):
    """
    Ratio of shorter normalized name length to longer length.

    Returns 1.0 for equal lengths and approaches 0 for
    very different lengths.
    """
    left_norm = normalize_for_comparison(left)
    right_norm = normalize_for_comparison(right)

    if not left_norm or not right_norm:
        return 0.0

    shorter = min(len(left_norm), len(right_norm))
    longer = max(len(left_norm), len(right_norm))

    if longer == 0:
        return 0.0

    return shorter / longer


def name_features(left, right):
    """
    Compute all name-based features for one candidate pair.
    """
    return {
        "name_exact": exact_match(left, right),
        "name_normalized_exact": normalized_exact_match(
            left, right
        ),
        "name_token_jaccard": token_jaccard(
            left, right
        ),
        "name_char_similarity": character_similarity(
            left, right
        ),
        "name_length_ratio": length_ratio(
            left, right
        ),
    }
