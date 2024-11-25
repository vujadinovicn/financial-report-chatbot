import os
import pandas as pd
import json

data_folder = "data"
form10k_folder = os.path.join(data_folder, "form10k")
form13_folder = os.path.join(data_folder, "form13")

for file in os.listdir(form13_folder):
    if file.endswith(".csv"):
        csv_path = os.path.join(form13_folder, file)
        df = pd.read_csv(csv_path)

        distinct_names = df['companyName'].dropna().unique().tolist()
        distinct_names = [name.strip() for name in distinct_names]
        json_file = file.replace(".csv", ".json")
        json_path = os.path.join(form10k_folder, json_file)

        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)

            json_data['names'] = distinct_names

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4)
        else:
            print(f"JSON file not found for {file}")
