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

        if match == '=' or '.' in match or ':' in match:
            formatted_part = f'{match}'
        elif match.startswith('-'):
            formatted_part = f'\n{match}'
        else:
            formatted_part = f'{match}'
        formatted_command += formatted_part

    # 在输入框中显示格式化的结果
    command_entry.setPlainText(formatted_command)

    # 对command进行分析，提取home目录信息
    match = re.search(r'-Dcatalina\.home=([^ ]+)', command)
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
analyze_button.clicked.connect(extract_catalina_home)
layout.addWidget(analyze_button)

# 创建结果文本框
result_text = QTextEdit()
result_text.setReadOnly(True)
result_text.setFixedHeight(100)  # 调整输出框的高度为100
layout.addWidget(result_text)

# 设置窗口布局
window.setLayout(layout)

# 显示窗口
window.show()

# 初始命令示例
command_entry.setPlainText("/usr/local/webserver/jdk1.8.0_191/bin/java|/usr/local/webserver/jdk1.8.0_191/bin/java -Djava.util.logging.config.file=/usr/local/webserver/apache-tomcat-9.0.63/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 -Dignore.endorsed.dirs= -classpath /usr/local/webserver/apache-tomcat-9.0.63/bin/bootstrap.jar:/usr/local/webserver/apache-tomcat-9.0.63/bin/tomcat-juli.jar -Dcatalina.base=/usr/local/webserver/apache-tomcat-9.0.63 -Dcatalina.home=/usr/local/webserver/apache-tomcat-9.0.63 -Djava.io.tmpdir=/usr/local/webserver/apache-tomcat-9.0.63/temp org.apache.catalina.startup.Bootstrap start")

# 运行主循环
app.exec_()
