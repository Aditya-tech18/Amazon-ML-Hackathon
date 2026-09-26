from entity_resolution.src.features.address_features import (
    address_features,
)


examples = [
    (
        "KH NO. -570/13, NEW DELHI, WEST DELHI",
        "KH NO 570/13 NEW DELHI WEST DELHI",
    ),
    (
        "105 ELM ST, MORGANTON, NC",
        "105 Elm Street, Morganton, NC",
    ),
    (
        "G-3/571, GULMOHAR COLONY, BHOPAL",
        "G-3/571 Gulmohar Colony Bhopal",
    ),
    (
        "105 ELM ST, MORGANTON, NC",
        "500 MARKET STREET, NEW YORK",
    ),
    (
        None,
        "500 MARKET STREET, NEW YORK",
    ),
]


print("=" * 70)
print("ADDRESS FEATURE TEST")
print("=" * 70)

for left, right in examples:
    print("\nLEFT :", left)
    print("RIGHT:", right)

    features = address_features(left, right)

    for name, value in features.items():
        print(f"{name:30} : {value:.4f}")
