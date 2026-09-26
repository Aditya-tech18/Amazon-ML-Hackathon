from entity_resolution.src.features.normalization import (
    normalize_text,
    normalize_for_comparison,
    tokenize,
    extract_numeric_tokens,
)


examples = [
    "ABC Restaurant Pvt. Ltd.",
    "ABC RESTAURANT PRIVATE LIMITED",
    "  ABC   Restaurant  ",
    "Moncada Léarning Center",
    "KH NO. -570/13, NEW DELHI",
]


print("=" * 70)
print("NORMALIZATION TEST")
print("=" * 70)

for text in examples:
    print("\nOriginal   :", text)
    print("Normalized :", normalize_text(text))
    print(
        "Comparison :",
        normalize_for_comparison(text),
    )
    print("Tokens     :", tokenize(text))
    print(
        "Numbers    :",
        extract_numeric_tokens(text),
    )
