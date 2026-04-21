import argparse
import os
import tempfile
from pathlib import Path

import pandas as pd
import numpy as np
import re


os.environ["MPLCONFIGDIR"] = str(Path(tempfile.gettempdir()) / "company_dashboard_mpl_cache")

import matplotlib.pyplot as plt


def to_number(text):
    text = str(text).lower().replace(",", "").strip()
    match = re.search(r"(\d+(\.\d+)?)", text)
    if not match:
        return np.nan

    value = float(match.group(1))

    if "k" in text:
        value *= 1000
    elif "lakh" in text or "lac" in text:
        value *= 100000
    elif "crore" in text or "cr" in text:
        value *= 10000000

    return value


def clean_hq(text):
    text = str(text).split("+")[0]
    text = re.sub(r"\.\s*", ", ", text)
    text = re.sub(r"\s*,\s*", ", ", text)
    return text.strip(" ,")


def extract_number(text):
    match = re.search(r"\d+", str(text))
    return float(match.group()) if match else np.nan


def employee_count(text):
    text = str(text).lower().replace("employees", "").strip()

    if "-" in text:
        parts = text.split("-")
        nums = [to_number(p) for p in parts]
        nums = [n for n in nums if not np.isnan(n)]
        return sum(nums) / len(nums) if nums else np.nan

    return to_number(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    df = df.sample(min(10, len(df)), random_state=args.seed).reset_index(drop=True)

    df["ratings"] = pd.to_numeric(df["ratings"], errors="coerce")
    df["review_num"] = df["review_count"].apply(to_number)
    df["years_num"] = df["years"].apply(extract_number)
    df["employees_num"] = df["employees"].apply(employee_count)
    df["hq_clean"] = df["hq"].apply(clean_hq)

    df = df.dropna(subset=["ratings", "review_num", "years_num", "employees_num", "hq_clean"]).reset_index(drop=True)

    print("\n1. Headquarters Of Chosen Companies")
    for i, row in df.iterrows():
        print(f"{i+1}. {row['name']} - {row['hq_clean']}")

    # 2. Ratings Bar Chart
    df2 = df.sort_values("ratings", ascending=False)
    plt.figure(figsize=(12, 6))
    plt.bar(df2["name"], df2["ratings"])
    plt.title("2. Company Ratings")
    plt.xlabel("Companies")
    plt.ylabel("Ratings")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # 3. Reviews Funnel
    df3 = df.sort_values("review_num", ascending=False)
    widths = df3["review_num"].to_numpy()
    left = (widths.max() - widths) / 2
    plt.figure(figsize=(12, 6))
    plt.barh(df3["name"], widths, left=left)
    plt.title("3. Company Reviews")
    plt.xlabel("Review Count")
    plt.ylabel("Companies")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    # 4. Employee Line Chart
    df4 = df.sort_values("employees_num")
    plt.figure(figsize=(12, 6))
    plt.plot(df4["name"], df4["employees_num"], marker="o")
    plt.title("4. Employee Count")
    plt.xlabel("Companies")
    plt.ylabel("Employee Count")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # 5. Pie Chart
    df5 = df.head(5)
    plt.figure(figsize=(8, 8))
    plt.pie(df5["years_num"], labels=df5["name"], autopct="%1.1f%%")
    plt.title("5. Company Years")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
