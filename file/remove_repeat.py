import os


def delete_files_with_parentheses(directory):
    # 获取目录中的所有文件
    files = os.listdir(directory)

    count = 0
    for file_name in files:
        # 检查文件名中是否包含括号字符
        if '(' in file_name and ')' in file_name:
            # 构建文件的完整路径
            file_path = os.path.join(directory, file_name)
            try:
                count += 1
                # 删除文件,不会在回收站中
                # 如果希望在回收站中删除文件，可以使用 send2trash 模块， from send2trash import send2trash
                # send2trash(file_path)

                os.remove(file_path)
                print(f"文件 '{file_name}' 已被删除.")
            except Exception as e:
                print(f"删除文件 '{file_name}' 时出现错误: {e}")

    print(f"共删除了 {count} 个文件.")


if __name__ == '__main__':
    directory_to_clean = '/Volumes/Elements SE/photos'
    delete_files_with_parentheses(directory_to_clean)
