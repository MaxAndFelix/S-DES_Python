from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from ui_main import Ui_Form


class Main:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = uic.loadUi("Forms/main.ui")

        # 使用界面定义的控件，也是从ui里面访问


app = QApplication([])
main = Main()
main.ui.show()
app.exec_()
