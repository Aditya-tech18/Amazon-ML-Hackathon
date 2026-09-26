from pathlib import Path
import pandas as pd

BASE = Path("student_resource/dataset/train")

FILES = {
    "source1": BASE / "train_source1.tsv",
    "source2": BASE / "train_source2.tsv",
    "source3": BASE / "train_source3.tsv",
    "ground_truth": BASE / "train_ground_truth.tsv",
}


def inspect_file(name, path):
    print(f"\n{'=' * 70}")
    print(f"{name.upper()}")
    print(f"{'=' * 70}")
    print(f"File: {path}")

    # Only read a small sample — never load the complete large TSV.
    df = pd.read_csv(path, sep="\t", nrows=5000, dtype=str)

    print(f"Columns: {list(df.columns)}")
    print(f"Sample rows: {len(df):,}")
    print("\nMissing values in sample:")
    print(df.isna().sum())

    print("\nSample:")
    print(df.head(3).to_string(index=False))


def main():
    for name, path in FILES.items():
        inspect_file(name, path)


if __name__ == "__main__":
    main()
