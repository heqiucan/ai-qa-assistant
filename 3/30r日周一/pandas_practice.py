import pandas as pd

# 使用绝对路径读取桌面上的文件（注意：如果你电脑用户名不是 16620，请修改）
file_path = r"C:\Users\16620\OneDrive\Desktop\成绩表.csv"
df = pd.read_csv(file_path, encoding='utf-8')

print("原始数据：")
print(df)
print("\n列名：", df.columns.tolist())

# 筛选语文 > 80 的行
try:
    high = df[df['语文'] > 80]   # 直接用 df[条件] 更简单
    print("\n语文 > 80 的同学：")
    print(high)
except KeyError as e:
    print(f"\n错误：列名 '{e}' 不存在，请检查 CSV 第一行是否包含 '语文' 列。")

# 新增总分列
df['总分'] = df['语文'] + df['数学'] + df['英语']
print("\n添加总分列后的数据：")
print(df)

# 按班级分组计算平均分
class_avg = df.groupby('班级')[['语文', '数学', '英语', '总分']].mean()
print("\n班级平均分：")
print(class_avg)

# 保存结果
class_avg.to_csv("班级平均分.csv", encoding='utf-8-sig')
print("\n结果已保存到 班级平均分.csv")