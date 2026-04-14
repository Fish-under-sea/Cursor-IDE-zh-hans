# -*- coding: utf-8 -*-
"""
Cursor 菜单硬编码字符串汉化脚本
用于将右键菜单中的硬编码英文文本替换为中文
注意：每次 Cursor 更新后需要重新运行此脚本检查
"""

import sys
import os

WORKBENCH_FILE = r"C:\Program Files (x86)\OTHER APP\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js"

# 定义替换规则 (英文原文 -> 中文翻译)
# 格式: ('"英文原文"', '"中文翻译"')
REPLACEMENTS = [
    # === 聊天相关 ===
    ('"Add Symbol to Current Chat..."', '"将符号添加到当前聊天..."'),
    ('"Add Symbol to New Chat..."', '"将符号添加到新聊天..."'),
    ('"Copilot Chat"', '"Copilot 对话"'),
    ('"Cursor Chat"', '"Cursor 聊天"'),
    ('"Cursor Agent"', '"Cursor 智能体"'),

    # === GitHub 相关 ===
    ('"View on GitHub"', '"在 GitHub 上查看"'),
    ('"Open on GitHub"', '"在 GitHub 上打开"'),
    ('"Copy GitHub Link"', '"复制 GitHub 链接"'),
    ('"Create Pull Request"', '"创建拉取请求"'),
    ('"View Pull Request"', '"查看拉取请求"'),

    # === 文件操作 ===
    ('"View File History"', '"查看文件历史"'),
    ('"Show in Explorer"', '"在资源管理器中显示"'),
    ('"Reveal in File Explorer"', '"在文件资源管理器中显示"'),

    # === Python 相关 ===
    ('"Add as Python Project"', '"添加为 Python 项目"'),
    ('"Python Interactive"', '"Python 交互式"'),
    ('"Interactive Window"', '"交互式窗口"'),
]

def main():
    print("=== Cursor 菜单汉化脚本 ===\n")
    print("注意：此脚本需要管理员权限运行\n")

    # 读取文件
    try:
        with open(WORKBENCH_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件\n{WORKBENCH_FILE}")
        print("\n请确认 Cursor 已安装且路径正确。")
        sys.exit(1)
    except PermissionError:
        print(f"错误：没有权限读取文件\n{WORKBENCH_FILE}")
        print("\n请以管理员身份运行此脚本。")
        sys.exit(1)

    original_len = len(content)
    total_replaced = 0
    replacements_made = []

    for old, new in REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            total_replaced += count
            replacements_made.append(f"  [OK] {old} -> {new} ({count}x)")

    if total_replaced == 0:
        print("未找到需要替换的字符串（可能已经汉化或 Cursor 版本已更新）")
        print("\n已知可汉化的菜单项：")
        for old, new in REPLACEMENTS:
            print(f"  • {old}")
        sys.exit(0)

    print(f"找到 {total_replaced} 处需要替换：\n")
    for r in replacements_made:
        print(r)

    # 写回文件
    try:
        with open(WORKBENCH_FILE, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
        print(f"\n替换完成！")
        print(f"文件大小: {original_len:,} -> {len(content):,} 字节")
        print("\n请重启 Cursor 查看效果。")
    except PermissionError:
        print(f"\n错误：没有权限写入文件\n{WORKBENCH_FILE}")
        print("\n请以管理员身份运行此脚本。")
        print("\n替代方案：")
        print("1. 右键点击 Cursor 快捷方式，选择'以管理员身份运行'")
        print("2. 然后重新运行此脚本")
        sys.exit(1)

if __name__ == "__main__":
    main()
