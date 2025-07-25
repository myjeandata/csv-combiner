import pandas as pd
import glob

files = glob.glob("data/*.csv")
dfs = [pd.read_csv(f) for f in files]

combined = pd.concat(dfs, ignore_index=True)
combined.to_csv("combined_sales.csv", index=False)
