import os
folder_path=r'C:\Users\16620\OneDrive\Desktop\my files'
filename="file1.text"
file_path=os.path.join(folder_path,filename)
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)