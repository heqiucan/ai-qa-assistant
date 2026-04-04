import os#os模块，用于文件路径
import pandas as pd#pandas模块用于创建和输出数据表

# 输入：文件夹路径（改成你自己的）
folder_path = r"C:\Users\16620\OneDrive\Desktop\(2)\my files"#folder_path是处理文件夹的路径，r是防止斜杠被转义

# 输出：合并后的文件路径
output_path = os.path.join(folder_path, "merged.txt")#文件夹的路径和文件名拼成完整路径，目的是生成的路径会自动加、

# 1. 收集所有 txt 文件
txt_files = []
for root, dirs, files in os.walk(folder_path):#os.walk会遍历folder_path下的所有子文件
    for file in files:#遍历当前当前文件夹的每一个文件
        if file.endswith('.txt') and file!="merged.txt":#只保留文件名以.txt结尾的文件
            txt_files.append(os.path.join(root, file))#存入txt_file

print("找到以下 txt 文件：")
for f in txt_files:
    print("  ", f)
stats ={}

# 2. 合并内容
with open(output_path, 'w', encoding='utf-8') as out:
    for file_path in txt_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 写入文件名作为分隔线
        filename = os.path.basename(file_path)
        out.write(f'--- {filename} ---\n')
        out.write(content)
        out.write('\n\n')
        line_count=content.count('\n')+(1 if content and not content.endswith('\n')else 0)# 空一行分隔
        stats[filename]=line_count

print(f"合并完成！结果保存在：{output_path}")
df=pd.DataFrame(list(stats.items()),columns=['文件名','行数'])
print("\n文件行数统计:")
print(df)
df.to_csv(os.path.join(folder_path,"行数统计.csv"),index=False,encoding='utf-8')
print(f"统计表已保存为:{os.path.join(folder_path,"行数统计.csv")}")
