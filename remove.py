import os

def process_mp4_files(directory):
    # 遍历给定目录下的所有文件和子目录
    for filename in os.listdir(directory):
        if filename.endswith('.mp4'):
            # 构建完整的文件路径
            file_path = os.path.join(directory, filename)
            
            # 如果文件名不以'_compressed.mp4'结尾
            if not filename.endswith('_compressed.mp4'):
                print(f"Deleting: {file_path}")
                # 删除文件
                os.remove(file_path)
            else:
                # 计算新的文件名
                new_filename = filename.replace('_compressed.mp4', '.mp4')
                new_file_path = os.path.join(directory, new_filename)
                
                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_path} -> {new_file_path}")

# 使用方法
# 将这里的 'your_directory_path' 替换为你的目标文件夹路径
process_mp4_files('supply1')