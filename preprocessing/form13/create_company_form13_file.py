import pandas as pd

file_path = "data/all_merged_tables.tsv"
data = pd.read_csv(file_path, sep="\t")

for cik, group in data.groupby("CIK"):
    company_name = group["companyName"].iloc[0].split(" ")[0].lower()
    file_name = f"data/form13/{company_name}-{str(cik).zfill(10)}.csv"
    group.to_csv(file_name, index=False)
    print(f"Saved: {file_name}")
