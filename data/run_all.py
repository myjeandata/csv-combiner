from pathlib import Path
import pandas as pd

# 현재 파일이 있는 폴더(data) 기준
DATA = Path(__file__).resolve().parent

# 1) CSV 합치기
csv_files = sorted([p for p in DATA.glob("file*.csv") if p.is_file()])
frames = [pd.read_csv(p) for p in csv_files]
combined = pd.concat(frames, ignore_index=True)
combined.to_csv(DATA / "combined_sales.csv", index=False)

# 2) 분석하기
df = pd.read_csv(DATA / "combined_sales.csv")
avg_age = df["age"].mean()
sum_age = df["age"].sum()

print(f"평균 나이: {avg_age:.2f}")
print(f"나이 합계: {sum_age}")

# 3) 결과 저장
summary = pd.DataFrame({"average_age": [avg_age], "total_age": [sum_age]})
summary.to_csv(DATA / "sales_summary.csv", index=False)
summary.to_excel(DATA / "sales_summary.xlsx", index=False)

print("모든 작업이 완료되었습니다.")