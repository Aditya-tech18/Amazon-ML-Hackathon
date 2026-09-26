import re
import unicodedata


def normalize_text(value):
    """
    General text normalization.

    Goals:
    - handle missing values
    - normalize Unicode
    - lowercase text
    - remove punctuation noise
    - normalize whitespace
    """

    if value is None:
        return ""

    if not isinstance(value, str):
        value = str(value)

    value = value.strip()

    if not value:
        return ""

    # Unicode normalization
    value = unicodedata.normalize("NFKC", value)

    # Lowercase
    value = value.lower()

    # Convert punctuation into spaces
    value = re.sub(
        r"[^\w\s]",
        " ",
        value,
        flags=re.UNICODE,
    )

    # Collapse repeated whitespace
    value = re.sub(r"\s+", " ", value).strip()

    return value


def normalize_for_comparison(value):
    """
    Compact representation for character-level comparison.
    """

    value = normalize_text(value)

    return value.replace(" ", "")


def tokenize(value):
    """
    Return normalized tokens.
    """

    value = normalize_text(value)

    if not value:
        return set()

    return set(value.split())


def extract_numeric_tokens(value):
    """
    Extract numbers from addresses/names.

    Example:
    'KH NO. 570/13, NEW DELHI'
    -> {'570', '13'}
    """

    if value is None:
        return set()

    return set(re.findall(r"\d+", str(value)))
