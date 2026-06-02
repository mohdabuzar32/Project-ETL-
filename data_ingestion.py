import pandas as pd
import os

folder_path = r"C:\Users\dell\Desktop\Project (ETL)\data\raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder_path, file))

        print("\n" + "="*50)
        print("File:", file)
        print("Shape:", df.shape)
        print(df.dtypes)
        print(df.head())