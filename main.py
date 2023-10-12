# from PyQt5 import uic
from PyQt5.QtWidgets import *
from qfluentwidgets import FluentIcon

from cracker import Cracker
from ui_main import Ui_Form
from encrypt import *
from utils import *


# class Main():
# noinspection PyArgumentList


class Main(QWidget):
    def __init__(self):
        # 从UI定义中动态加载窗口对象
        # self.ui = uic.loadUi("Forms/main.ui")
        # 从文件中加载UI定义
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.cracker = None

        self.resize(400, 600)

        self.ui.rBtn_Bin.setChecked(True)
        self.ui.lineEdit_Key.setClearButtonEnabled(True)

        self.ui.pBtn_Github.setIcon(FluentIcon.GITHUB)
        self.ui.pBtn_Github.clicked.connect(lambda: openWebsite("https://github.com/MaxAndFelix/S-DES_Python"))
        self.ui.tBtn_Issue.setIcon(FluentIcon.FEEDBACK)
        self.ui.tBtn_Issue.setToolTip('提供反馈')
        self.ui.tBtn_Issue.setToolTipDuration(-1)
        self.ui.tBtn_Issue.clicked.connect(lambda: openWebsite("https://github.com/MaxAndFelix/S-DES_Python/issues"))

        self.ui.pBtn_Encrypt.clicked.connect(self.encrypt)
        self.ui.pBtn_Decrypt.clicked.connect(self.decrypt)
        self.ui.pBtn_Crack.clicked.connect(self.openCracker)

    def encrypt(self):
        self.ui.cypherTextEdit.clear()
        key = [int(char) for char in self.ui.lineEdit_Key.text()]
        plain_txt = self.ui.plainTextEdit.toPlainText()

        if self.ui.rBtn_Str.isChecked():
            plain_txt = str2asc(plain_txt)

        # 异常处理：
        if not plain_txt.strip():  # 使用strip()方法移除前后的空白字符并检查文本是否为空
            showErrorInfoBar(self, '明文为空，请输入')
            return
        if len(plain_txt) % 8 != 0 or not is_bin(plain_txt):
            showErrorInfoBar(self, '明文不是整数个Byte，请查证后再输入')
            return
        if len(self.ui.lineEdit_Key.text()) != 10 or not is_bin(self.ui.lineEdit_Key.text()):
            showErrorInfoBar(self, '密钥仅能为10位比特串')
            return

        for byte in bit2int(plain_txt):
            cypher_txt = main_encryption(
                plain_txt=byte,
                k=key
            )
            self.ui.cypherTextEdit.insertPlainText(int2txt(cypher_txt))

        if self.ui.rBtn_Str.isChecked():
            self.ui.cypherTextEdit.setPlainText(
                asc2str(self.ui.cypherTextEdit.toPlainText())
            )

    def decrypt(self):
        self.ui.plainTextEdit.clear()
        key = [int(char) for char in self.ui.lineEdit_Key.text()]
        cypher_txt = self.ui.cypherTextEdit.toPlainText()

        if self.ui.rBtn_Str.isChecked():
            cypher_txt = str2asc(cypher_txt)

        # 异常处理：
        if not cypher_txt.strip():  # 使用strip()方法移除前后的空白字符并检查文本是否为空
            showErrorInfoBar(self, '密文为空，请输入')
            return
        if len(cypher_txt) % 8 != 0 or not is_bin(cypher_txt):
            showErrorInfoBar(self, '密文不是整数个Byte，请查证后再输入')
            return
        if len(self.ui.lineEdit_Key.text()) != 10 or not is_bin(self.ui.lineEdit_Key.text()):
            showErrorInfoBar(self, '密钥仅能为10位比特串')
            return

        for byte in bit2int(cypher_txt):
            plain_txt = main_decryption(
                cypher_txt=byte,
                k=key
            )
            self.ui.plainTextEdit.insertPlainText(int2txt(plain_txt))

        if self.ui.rBtn_Str.isChecked():
            self.ui.plainTextEdit.setPlainText(
                asc2str(self.ui.plainTextEdit.toPlainText())
            )

    def openCracker(self):
        if self.cracker is None:  # 仅当Cracker窗口不存在时创建
            self.cracker = Cracker()
        self.cracker.show()


QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

app = QApplication([])
main = Main()
# main.ui.show()
main.show()
app.exec_()
