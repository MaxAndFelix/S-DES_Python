from PyQt5.QtWidgets import QApplication, QWidget
from ui_main import Ui_Form


class Main(QWidget):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问


app = QApplication([])
main = Main()
main.show()
app.exec_()
