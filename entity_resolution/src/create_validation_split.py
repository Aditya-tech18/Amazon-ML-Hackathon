from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


SOURCE1_PATH = Path(
    "student_resource/dataset/train/train_source1.tsv"
)

OUTPUT_DIR = Path("entity_resolution/artifacts/splits")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    print("Reading S1 entity IDs...")

    entity_ids = []

    for chunk in pd.read_csv(
        SOURCE1_PATH,
        sep="\t",
        dtype=str,
        usecols=["entity_id"],
        chunksize=200_000,
    ):
        entity_ids.extend(chunk["entity_id"].tolist())

    entity_ids = pd.Series(entity_ids, name="s1_id")

    train_ids, valid_ids = train_test_split(
        entity_ids,
        test_size=0.20,
        random_state=42,
        shuffle=True,
    )

    train_ids = train_ids.sort_values()
    valid_ids = valid_ids.sort_values()

    train_path = OUTPUT_DIR / "train_s1_ids.parquet"
    valid_path = OUTPUT_DIR / "valid_s1_ids.parquet"

    train_ids.to_frame().to_parquet(
        train_path,
        index=False,
    )

    valid_ids.to_frame().to_parquet(
        valid_path,
        index=False,
    )

    print("\nValidation split created")
    print("-" * 50)
    print(f"Total S1      : {len(entity_ids):,}")
    print(f"Train S1      : {len(train_ids):,}")
    print(f"Validation S1 : {len(valid_ids):,}")
    print(f"Train ratio   : {len(train_ids) / len(entity_ids):.2%}")
    print(f"Valid ratio   : {len(valid_ids) / len(entity_ids):.2%}")

    print("\nSaved:")
    print(train_path)
    print(valid_path)


if __name__ == "__main__":
    main()
