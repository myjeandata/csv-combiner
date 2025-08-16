import pandas as pd
import os

# CSV 파일들이 들어있는 폴더 경로
folder_path = 'data'

# 폴더 안의 모든 CSV 파일 불러오기
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# CSV 파일들을 하나로 합치기
df_list = [pd.read_csv(os.path.join(folder_path, file)) for file in all_files]
combined_df = pd.concat(df_list, ignore_index=True)

# 합친 파일 저장
combined_df.to_csv('combined_sales.csv', index=False, encoding='utf-8-sig')

print("모든 CSV 파일이 combined_sales.csv 로 합쳐졌습니다.")

