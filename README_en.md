# CSV Combiner

This is a simple Python project designed to combine multiple CSV files into one.

## Features

- Automatically detects and loads all `.csv` files in a specified folder (e.g., `data/`)
- Concatenates the contents into a single DataFrame
- Preserves all headers and rows from each file
- Exports the final combined result as `combined_sales.csv` in the same folder

## Technologies Used

- Python
- pandas
- glob

## Problem Statement

When managing monthly or daily sales data, files are often stored separately. It becomes inconvenient to analyze or summarize them one by one. This project solves that by merging them into one file for easier analysis.

## How It Works

1. All `.csv` files are saved in the `data/` folder.
2. The script `combine_files.py` is executed.
3. The script reads all the CSV files and merges them vertically.
4. A new file `combined_sales.csv` is created in the same folder.
