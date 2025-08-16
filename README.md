# CSV 데이터 통합 & 기본 통계 분석 (자동 실행)

## 개요
- /data 폴더의 CSV 파일들(`file*.csv`)을 자동으로 합칩니다.
- 합쳐진 데이터에서 `age` 컬럼의 **평균**과 **합계를** 계산합니다.
- 결과는 CSV/Excel 파일로 저장됩니다.

## 실행 방법
1) VS Code 하단 터미널에서 위치 이동  
2) 자동 실행  
3) 정상 실행 시 터미널 예시

## 입력 규칙
- /data 폴더에 **file1.csv, file2.csv, …** 형태의 CSV를 넣습니다.
- CSV에는 최소한 `age` 컬럼이 있어야 합니다. (정수/실수)

## 생성되는 파일
- `combined_sales.csv` : 모든 CSV를 합친 결과
- `sales_summary.csv` : 평균/합계 요약(CSV)
- `sales_summary.xlsx` : 평균/합계 요약(Excel)

## 폴더 구조(예)

## 스크린샷 가이드
- `img/01_run.png` : 터미널에 `python run_all.py` 실행 후 "평균/합계/완료"가 출력된 화면
- `img/02_summary.png` : Excel에서 `sales_summary.xlsx`가 열린 화면(average_age, total_age가 보이게)
- img/result.png : 분석 결과 이미지

## 참고
- `age` 컬럼명이 다를 경우, `run_all.py` 안의 `df["age"]`를 실제 컬럼명으로 변경하면 됩니다.

