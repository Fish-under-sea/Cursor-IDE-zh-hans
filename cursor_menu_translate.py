# Cursor 菜单硬编码字符串汉化脚本
# 用于将 "Add Symbol to Current Chat" 和 "Add Symbol to New Chat" 替换为中文
# 注意：每次 Cursor 更新后需要重新运行此脚本

import sys

WORKBENCH_FILE = r"C:\Program Files (x86)\OTHER APP\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js"

def main():
    print("=== Cursor 菜单汉化脚本 ===\n")

    # 读取文件
    try:
        with open(WORKBENCH_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件\n{WORKBENCH_FILE}")
        print("\n请确认 Cursor 已安装且路径正确。")
        sys.exit(1)
    except PermissionError:
        print(f"错误：没有权限修改文件\n{WORKBENCH_FILE}")
        print("\n请以管理员身份运行此脚本。")
        sys.exit(1)

    original_len = len(content)

    # 定义替换规则
    replacements = [
        ('"Add Symbol to Current Chat..."', '"将符号添加到当前聊天..."'),
        ('"Add Symbol to New Chat..."', '"将符号添加到新聊天..."'),
    ]

    total_replaced = 0
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            total_replaced += count
            print(f"已替换 {count}x: {old}")

    if total_replaced == 0:
        print("未找到需要替换的字符串（可能已经汉化或路径不正确）")
        sys.exit(0)

    # 写回文件
    try:
        with open(WORKBENCH_FILE, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
        print(f"\n替换完成！共替换 {total_replaced} 处")
        print(f"文件大小: {original_len} -> {len(content)}")
        print("\n请重启 Cursor 查看效果。")
    except PermissionError:
        print(f"\n错误：没有权限写入文件\n{WORKBENCH_FILE}")
        print("\n请以管理员身份运行此脚本。")
        sys.exit(1)

if __name__ == "__main__":
    main()
