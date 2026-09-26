from entity_resolution.src.features.country_features import (
    country_features,
)


examples = [
    ("US", "US"),
    ("India", "India"),
    ("US", "India"),
    ("France", "France"),
    (None, "India"),
]


print("=" * 70)
print("COUNTRY FEATURE TEST")
print("=" * 70)

for left, right in examples:
    print("\nLEFT :", left)
    print("RIGHT:", right)

    features = country_features(left, right)

    for name, value in features.items():
        print(f"{name:30} : {value:.4f}")
