# charts.py  (프로젝트 루트에 위치)
import os
import pandas as pd
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
CSV  = os.path.join(ROOT, "combined_sales.csv")
IMG  = os.path.join(ROOT, "data", "img")
os.makedirs(IMG, exist_ok=True)

# 데이터 로드
df = pd.read_csv(CSV)

# 컬럼명: date, product, amount
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])
df["year_month"] = df["date"].dt.to_period("M").astype(str)

# 1) 월별 매출 추세
monthly = df.groupby("year_month")["amount"].sum().reset_index()
plt.figure(figsize=(9,4.8))
plt.plot(monthly["year_month"], monthly["amount"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Amount")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(IMG, "01_monthly_sales.png"), dpi=150)
plt.close()

# 2) 제품별 매출 (Top 10)
by_prod = df.groupby("product")["amount"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(9,4.8))
by_prod.plot(kind="bar")
plt.title("Top Products by Sales")
plt.xlabel("Product")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig(os.path.join(IMG, "02_sales_by_product.png"), dpi=150)
plt.close()

print("[완료] data/img/01_monthly_sales.png, 02_sales_by_product.png 생성")

