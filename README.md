# csv-combiner

This is a simple Python script to combine multiple CSV files into one.

## Features

- Combines all `.csv` files from a folder into one file
- Maintains all headers and rows
- Saves the result as `all_data.csv` in the same folder

## How to use

1. Save all the `.csv` files you want to combine in one folder (e.g., `data/`)
2. Run the script `combine_files.py`
3. It will generate a new file called `all_data.csv`

## Sample Code

```python
import glob
import pandas as pd

# Step 1: Read all CSV files from the folder
files = glob.glob("data/*.csv")
dfs = [pd.read_csv(f) for f in files]

# Step 2: Combine them vertically
all_data = pd.concat(dfs, ignore_index=True)

# Step 3: Save the result
all_data.to_csv("all_data.csv", index=False)
```

## Requirements

- Python 3.x
- pandas

You can install pandas with:

```
pip install pandas
```
