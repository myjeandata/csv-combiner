# combine_files.py  (판매 데이터 전용, 깔끔한 합치기)
import csv, glob, os

INPUT_DIR = "data"
OUTPUT = "combined_sales.csv"
FIELDNAMES = ["date", "product", "amount"]

def iter_rows():
    # data 폴더의 sales_*.csv를 이름순으로 처리
    for path in sorted(glob.glob(os.path.join(INPUT_DIR, "sales_*.csv"))):
        with open(path, newline="", encoding="utf-8") as f:
            r = csv.reader(f)
            # 헤더 스킵
            header = next(r, None)
            for row in r:
                # 빈 줄 건너뛰기
                if not row or all(not str(c).strip() for c in row):
                    continue
                # 앞의 3개 컬럼만 사용 (date, product, amount)
                yield row[:3]

def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    with open(OUTPUT, "w", newline="", encoding="utf-8") as out:
        w = csv.writer(out)
        w.writerow(FIELDNAMES)  # 헤더 한 번만
        for row in iter_rows():
            w.writerow(row)
    print(f"[완료] {OUTPUT} 생성")

if __name__ == "__main__":
    main()


