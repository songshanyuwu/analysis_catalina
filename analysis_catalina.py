import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout

def extract_catalina_home():
    command = command_entry.toPlainText()

    # 使用正则表达式提取参数和值
    pattern = r'(-\w+|=|[\w.\-\/]+|[^\s=]+)'
    matches = re.findall(pattern, command)

    # 格式化输出命令的每个部分
    formatted_command = ''
    for match in matches:
        match = match.replace('\n', '')

        if match == '='  或者 '.' in match  或者 ':' in match:
            formatted_part = f'{match}'
        elif match.startswith('-'):
            formatted_part = f'\n{match}'
        else:
            formatted_part = f'{match}'
        formatted_command += formatted_part

    # 在输入框中显示格式化的结果
    command_entry.setPlainText(formatted_command)

    # 对command进行分析，提取home目录信息
    match = re.搜索(r'-Dcatalina\.home=([^ ]+)', command)
    if match:
        catalina_home = match.group(1)
        result_text.setPlainText(catalina_home)
    else:
        result_text.setPlainText(">> 在命令中没有发现Catalina的家目录 <<")

# 创建应用程序对象
app = QApplication([])

# 创建窗口
window = QWidget()
window.setWindowTitle("Catalina Home Extractor V0.1          songshanyuwu")
window.setFixedSize(600, 600)

# 创建布局
layout = QVBoxLayout()

# 创建标签和输入框
command_label = QLabel("请输入java启动命令:")
layout.addWidget(command_label)
command_entry = QTextEdit()
command_entry.setFixedHeight(380)  # 调整输入框的高度为400
layout.addWidget(command_entry)

# 创建分析按钮
analyze_button = QPushButton("分析Catalina家目录")
analyze_button.clicked。connect(extract_catalina_home)
layout.addWidget(analyze_button)

# 创建结果文本框
result_text = QTextEdit()
result_text.setReadOnly(True)
result_text.setFixedHeight(100)  # 调整输出框的高度为100
layout.addWidget(result_text)

# 设置窗口布局
window.setLayout(layout)

# 显示窗口
window.显示()

# 运行主循环
app.exec_()
