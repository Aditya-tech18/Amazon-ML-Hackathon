from pathlib import Path
from collections import Counter

import pandas as pd


GT_PATH = Path(
    "student_resource/dataset/train/train_ground_truth.tsv"
)


def main():
    total_s1 = 0
    no_match = 0
    total_links = 0

    s2_links = 0
    s3_links = 0

    match_distribution = Counter()

    for chunk in pd.read_csv(
        GT_PATH,
        sep="\t",
        dtype=str,
        chunksize=100_000,
        keep_default_na=False,
    ):
        for matched_ids in chunk["matched_entity_ids"]:
            matched_ids = matched_ids.strip()

            if not matched_ids:
                no_match += 1
                match_distribution[0] += 1
                total_s1 += 1
                continue

            ids = [
                entity_id.strip()
                for entity_id in matched_ids.split(",")
                if entity_id.strip()
            ]

            total_s1 += 1
            total_links += len(ids)
            match_distribution[len(ids)] += 1

            for entity_id in ids:
                if entity_id.startswith("S2-"):
                    s2_links += 1
                elif entity_id.startswith("S3-"):
                    s3_links += 1

    matched_s1 = total_s1 - no_match
    avg_links = total_links / total_s1
    avg_links_matched_only = (
        total_links / matched_s1
        if matched_s1
        else 0
    )

    print("=" * 70)
    print("GROUND TRUTH ANALYSIS")
    print("=" * 70)

    print(f"Total S1 entities          : {total_s1:,}")
    print(f"S1 entities with no match  : {no_match:,}")
    print(f"S1 entities with >=1 match : {matched_s1:,}")

    print(f"\nTotal positive links       : {total_links:,}")
    print(f"S2 positive links          : {s2_links:,}")
    print(f"S3 positive links          : {s3_links:,}")

    print(f"\nAverage links / S1         : {avg_links:.4f}")
    print(
        "Average links / matched S1: "
        f"{avg_links_matched_only:.4f}"
    )

    print("\nMatch-count distribution:")
    print("-" * 50)

    for count, frequency in sorted(match_distribution.items()):
        percentage = frequency / total_s1 * 100

        print(
            f"{count:3d} matches : "
            f"{frequency:12,} S1 "
            f"({percentage:6.2f}%)"
        )


if __name__ == "__main__":
    main()
