# 人机交互设计第三小组

这是第三小组的内部代码仓库，用来测试 Git 的**共享修改**功能。

## 运行测试代码

双击 `run.bat` 即可运行（需要已安装 Python 3），也可以手动执行：

```
python main.py
```

运行后会弹出一个对话框，显示：**欢迎阅读本小组的代码！**

## 如何测试共享修改

1. 组员 A 打开 `main.py`，把 `WELCOME_TEXT` 改成自己想说的话（或新建一个 `<姓名>.txt`）。
2. 组员 A 提交并推送：

   ```
   git pull
   git add .
   git commit -m "修改了欢迎语"
   git push
   ```

3. 组员 B 执行 `git pull`，再运行 `python main.py`，就能看到 A 的改动。

## 目录说明

| 文件 | 说明 |
| --- | --- |
| `main.py` | 测试用的主程序，运行后弹出欢迎对话框 |
| `run.bat` | Windows 下双击即可运行的启动脚本 |
| `README.md` | 本说明文件 |
