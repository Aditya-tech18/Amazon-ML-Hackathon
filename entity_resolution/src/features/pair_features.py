from entity_resolution.src.features.name_features import (
    name_features,
)

from entity_resolution.src.features.address_features import (
    address_features,
)

from entity_resolution.src.features.country_features import (
    country_features,
)


def pair_features(
    s1_name,
    candidate_name,
    s1_address,
    candidate_address,
    s1_country,
    candidate_country,
):
    features = {}

    features.update(
        name_features(
            s1_name,
            candidate_name,
        )
    )

    features.update(
        address_features(
            s1_address,
            candidate_address,
        )
    )

    features.update(
        country_features(
            s1_country,
            candidate_country,
        )
    )

    # Cross-field features

    features["name_address_agreement"] = (
        features["name_char_similarity"]
        * features["address_char_similarity"]
    )

    features["name_country_agreement"] = (
        features["name_char_similarity"]
        * features["country_match"]
    )

    features["address_country_agreement"] = (
        features["address_char_similarity"]
        * features["country_match"]
    )

    return features
