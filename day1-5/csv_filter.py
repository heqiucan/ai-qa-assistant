import pandas as pd
file_path = r'C:\Users\16620\OneDrive\Desktop\my files\sales.csv'
df= pd.read_csv(file_path)
print(df.head())
filtered=df[df["销量"]>50]
print("筛选结果:")
print(filtered)
filtered.to_csv('销量大于50.csv',index=False,encoding='utf_8')
print("已保存")