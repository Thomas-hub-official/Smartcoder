# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Smartcoder.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(794, 399)
        self.input_text_edit = QtWidgets.QPlainTextEdit(Dialog)
        self.input_text_edit.setGeometry(QtCore.QRect(20, 40, 501, 151))
        self.input_text_edit.setPlainText("")
        self.input_text_edit.setObjectName("input_text_edit")
        self.decode = QtWidgets.QRadioButton(Dialog)
        self.decode.setGeometry(QtCore.QRect(680, 310, 115, 19))
        self.decode.setObjectName("decode")
        self.encode = QtWidgets.QRadioButton(Dialog)
        self.encode.setGeometry(QtCore.QRect(550, 310, 115, 19))
        self.encode.setObjectName("encode")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 260, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.output_text_edit = QtWidgets.QTextEdit(Dialog)
        self.output_text_edit.setGeometry(QtCore.QRect(20, 230, 501, 151))
        self.output_text_edit.setObjectName("output_text_edit")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(600, 40, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 340, 241, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(540, 40, 54, 28))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(540, 80, 221, 171))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decode.setText(_translate("Dialog", "Decode"))
        self.encode.setText(_translate("Dialog", "Encode"))
        self.pushButton.setText(_translate("Dialog", "Convert"))
        self.label.setText(_translate("Dialog", "Input Text"))
        self.label_2.setText(_translate("Dialog", "Output Text"))
        self.pushButton_3.setText(_translate("Dialog", "Smart Test"))
        self.label_3.setText(_translate("Dialog", "Search"))