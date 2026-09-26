from entity_resolution.src.features.pair_features import (
    pair_features,
)


s1 = {
    "business_name": "ABC Restaurant Pvt. Ltd.",
    "business_address": "105 ELM ST, MORGANTON, NC",
    "country": "US",
}

candidate = {
    "business_name": "ABC Restaurant Private Limited",
    "business_address": "105 Elm Street, Morganton, NC",
    "country": "US",
}


features = pair_features(
    s1_name=s1["business_name"],
    candidate_name=candidate["business_name"],
    s1_address=s1["business_address"],
    candidate_address=candidate["business_address"],
    s1_country=s1["country"],
    candidate_country=candidate["country"],
)


print("=" * 70)
print("COMPLETE PAIR FEATURE TEST")
print("=" * 70)

print(f"Total features: {len(features)}")

print("\nFeature values:")
print("-" * 70)

for name, value in features.items():
    print(f"{name:35} : {value:.4f}")
