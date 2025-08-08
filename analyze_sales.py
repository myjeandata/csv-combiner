import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("combined_sales.csv")

# 기본 정보 출력
print("👉 데이터 요약")
print(df.info())

print("\n👉 앞부분 미리 보기")
print(df.head())

print("\n👉 날짜별 매출 합계")
print(df.groupby("Date")["Sales"].sum())

print("\n👉 상품별 총 판매 수량")
print(df["Product"].value_counts())