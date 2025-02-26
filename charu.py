def insert_content_before_each_line():
    filename = input("请输入txt文件名（如input.txt ）: ").strip()
    insert_content = input("请输入要插入的内容: ").strip()

    # 读取原文件行内容
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines() 

    # 构建新内容（每行前插入新内容）
    new_lines = []
    for line in lines:
        new_lines.append(f"{insert_content}\n") 
        new_lines.append(line) 

    # 写入新文件
    new_filename = f"new_{filename}"
    with open(new_filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines) 

    print(f"生成新文件: {new_filename}")

if __name__ == "__main__":
    insert_content_before_each_line()