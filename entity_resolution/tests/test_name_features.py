from entity_resolution.src.features.name_features import (
    name_features,
)


examples = [
    (
        "ABC Restaurant Pvt. Ltd.",
        "ABC Restaurant Private Limited",
    ),
    (
        "ABC Restaurant",
        "ABC Restaurant",
    ),
    (
        "Moyna's Coffee",
        "Moynas Coffee",
    ),
    (
        "ABC Restaurant",
        "XYZ Plumbing",
    ),
]


print("=" * 70)
print("NAME FEATURE TEST")
print("=" * 70)

for left, right in examples:
    print("\nLEFT :", left)
    print("RIGHT:", right)

    features = name_features(left, right)

    for name, value in features.items():
        print(f"{name:25} : {value:.4f}")
