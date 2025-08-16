from pathlib import Path
import pandas as pd

# 이 파일과 같은 폴더(data)를 기준으로 처리
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / 'combined_sales.csv'      # 입력 CSV: data/combined_sales.csv
out_path = BASE_DIR / 'sales_summary.csv'       # 출력 CSV: data/sales_summary.csv

# CSV 읽기
df = pd.read_csv(csv_path)

# 컬럼 이름이 정확히 'age'인지 확인 (문제 시 주석 해제하여 확인)
# print(df.columns)

# 계산
avg_age = df['age'].mean()
sum_age = df['age'].sum()

# 결과 출력
print(f"평균 나이: {avg_age}")
print(f"나이 합계: {sum_age}")

# 결과 저장 (data 폴더에 저장)
summary_df = pd.DataFrame({'average_age': [avg_age], 'total_age': [sum_age]})
summary_df.to_csv(out_path, index=False)
print(f"평균 나이: {avg_age:.2f}")
print(f"나이 합계: {sum_age}")
print(f"완료: {out_path}")