import os

folder_path = r"C:\Users\16620\OneDrive\Desktop\my files"
file_names = ["file1.text", "file2.text", "file3.text"]
output_path = os.path.join(folder_path, "all.txt")

with open(output_path, "w", encoding="utf-8") as out:
    for name in file_names:
        file_path = os.path.join(folder_path, name)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        out.write(f"=== 来自文件 {name} ===\n")
        out.write(content + "\n\n")

print("合并完成！结果保存在：", output_path)