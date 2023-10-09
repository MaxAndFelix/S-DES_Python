# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Forms/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(600, 400)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Plain = QtWidgets.QLabel(Form)
        self.label_Plain.setObjectName("label_Plain")
        self.verticalLayout_3.addWidget(self.label_Plain)
        self.PlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.PlainTextEdit.setPlainText("")
        self.PlainTextEdit.setObjectName("PlainTextEdit")
        self.verticalLayout_3.addWidget(self.PlainTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pBtn_Encrypt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn_Encrypt.sizePolicy().hasHeightForWidth())
        self.pBtn_Encrypt.setSizePolicy(sizePolicy)
        self.pBtn_Encrypt.setMinimumSize(QtCore.QSize(30, 0))
        self.pBtn_Encrypt.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pBtn_Encrypt.setObjectName("pBtn_Encrypt")
        self.verticalLayout.addWidget(self.pBtn_Encrypt)
        self.pBtn_Decrypt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn_Decrypt.sizePolicy().hasHeightForWidth())
        self.pBtn_Decrypt.setSizePolicy(sizePolicy)
        self.pBtn_Decrypt.setMinimumSize(QtCore.QSize(30, 0))
        self.pBtn_Decrypt.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pBtn_Decrypt.setObjectName("pBtn_Decrypt")
        self.verticalLayout.addWidget(self.pBtn_Decrypt)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_cipher = QtWidgets.QLabel(Form)
        self.label_cipher.setObjectName("label_cipher")
        self.verticalLayout_2.addWidget(self.label_cipher)
        self.CipherTextBrowser = QtWidgets.QTextBrowser(Form)
        self.CipherTextBrowser.setObjectName("CipherTextBrowser")
        self.verticalLayout_2.addWidget(self.CipherTextBrowser)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Crack = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Crack.sizePolicy().hasHeightForWidth())
        self.label_Crack.setSizePolicy(sizePolicy)
        self.label_Crack.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_Crack.setObjectName("label_Crack")
        self.horizontalLayout.addWidget(self.label_Crack)
        self.pBtn_Crack = QtWidgets.QPushButton(Form)
        self.pBtn_Crack.setObjectName("pBtn_Crack")
        self.horizontalLayout.addWidget(self.pBtn_Crack)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "S-DES"))
        self.label_Plain.setText(_translate("Form", "明文"))
        self.PlainTextEdit.setPlaceholderText(_translate("Form", "在此键入明文"))
        self.pBtn_Encrypt.setText(_translate("Form", "→加密→"))
        self.pBtn_Decrypt.setText(_translate("Form", "←解密←"))
        self.label_cipher.setText(_translate("Form", "密文"))
        self.label_Crack.setText(_translate("Form", "已有明密文对？"))
        self.pBtn_Crack.setText(_translate("Form", "暴力破解"))
