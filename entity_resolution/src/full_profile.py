from pathlib import Path
import pandas as pd
from collections import Counter

BASE = Path("student_resource/dataset/train")

FILES = {
    "source1": BASE / "train_source1.tsv",
    "source2": BASE / "train_source2.tsv",
    "source3": BASE / "train_source3.tsv",
}


def profile_entity_file(name, path):
    print("\n" + "=" * 70)
    print(name.upper())
    print("=" * 70)

    total_rows = 0
    missing_name = 0
    missing_address = 0
    missing_country = 0

    countries = Counter()
    duplicate_ids = 0
    seen_ids = set()

    for chunk in pd.read_csv(
        path,
        sep="\t",
        dtype=str,
        chunksize=100_000,
        keep_default_na=True,
    ):
        total_rows += len(chunk)

        missing_name += chunk["business_name"].isna().sum()
        missing_address += chunk["business_address"].isna().sum()
        missing_country += chunk["country"].isna().sum()

        countries.update(chunk["country"].fillna("<MISSING>").str.strip())

        for entity_id in chunk["entity_id"].dropna():
            if entity_id in seen_ids:
                duplicate_ids += 1
            seen_ids.add(entity_id)

    print(f"Total rows       : {total_rows:,}")
    print(f"Unique entity IDs: {len(seen_ids):,}")
    print(f"Duplicate IDs    : {duplicate_ids:,}")

    print("\nMissing values:")
    print(f"business_name    : {missing_name:,}")
    print(f"business_address : {missing_address:,}")
    print(f"country          : {missing_country:,}")

    print("\nCountry distribution:")
    for country, count in countries.most_common():
        percentage = count / total_rows * 100
        print(f"{country:15} {count:12,} ({percentage:6.2f}%)")


def profile_ground_truth(path):
    print("\n" + "=" * 70)
    print("GROUND TRUTH")
    print("=" * 70)

    total_rows = 0
    empty_matches = 0
    match_counts = Counter()
    invalid_rows = 0

    for chunk in pd.read_csv(
        path,
        sep="\t",
        dtype=str,
        chunksize=100_000,
        keep_default_na=False,
    ):
        total_rows += len(chunk)

        for value in chunk["matched_entity_ids"]:
            value = str(value).strip()

            if not value:
                empty_matches += 1
                match_counts[0] += 1
                continue

            ids = [
                x.strip()
                for x in value.split(",")
                if x.strip()
            ]

            match_counts[len(ids)] += 1

            for entity_id in ids:
                if not (
                    entity_id.startswith("S2-")
                    or entity_id.startswith("S3-")
                ):
                    invalid_rows += 1

    print(f"Total S1 rows       : {total_rows:,}")
    print(f"No-match rows       : {empty_matches:,}")
    print(f"Invalid match IDs   : {invalid_rows:,}")

    print("\nMatches per S1:")
    for count, frequency in sorted(match_counts.items()):
        percentage = frequency / total_rows * 100
        print(
            f"{count:3d} matches -> "
            f"{frequency:12,} S1 entities "
            f"({percentage:6.2f}%)"
        )


def main():
    for name, path in FILES.items():
        profile_entity_file(name, path)

    profile_ground_truth(
        BASE / "train_ground_truth.tsv"
    )


if __name__ == "__main__":
    main()
