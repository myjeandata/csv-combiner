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

## 📊 Sample Analysis

다음은 결합된 CSV 데이터를 분석한 간단한 예시입니다.

예시 파일에는 날짜별 매출 데이터가 들어 있으며, `combined_sales.csv` 파일로 통합되었습니다.

### ✅ 예시 질문: 가장 매출이 높았던 날짜는?

```python
import pandas as pd

df = pd.read_csv("combined_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
result = df.groupby("Date")["Amount"].sum().sort_values(ascending=False)
print(result.head(1))