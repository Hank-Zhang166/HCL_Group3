# -*- coding: utf-8 -*-
"""人机交互设计第三小组 —— 共享修改功能测试代码。

运行方式（任选其一）：
    1. 双击 run.bat
    2. 在命令行执行：python main.py

运行后会弹出一个对话框，显示欢迎信息。
本文件专门用来测试 Git 仓库的“共享修改”功能：
每位组员都可以修改下面的 WELCOME_TEXT（或新增自己的文件），
然后通过 git pull / git commit / git push 查看改动是否同步。
"""

import tkinter as tk
from tkinter import messagebox

# 只要改动这一行，就能测试共享修改是否同步到其他人那里
WELCOME_TEXT = "欢迎阅读本小组的代码！"


def show_welcome(text: str = WELCOME_TEXT) -> None:
    """弹出一个对话框，显示欢迎信息。"""
    root = tk.Tk()
    root.withdraw()  # 隐藏多余的主窗口，只留下对话框
    messagebox.showinfo("人机交互设计第三小组", text)
    root.destroy()


if __name__ == "__main__":
    show_welcome()
