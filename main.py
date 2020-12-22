import sys, os
import hashlib
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                             QLineEdit, QPushButton, QGridLayout, QAbstractItemView, QListWidget)
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import Qt, QRegExp
from Smartcoder import *
from methods import *


class MainWindow(QWidget, Ui_Dialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.ui()
        self.setWindowTitle('Thomas Smartcoder-v1.4')

        self.final = ''
        self.original = ''
        self.final = ''
        self.method = ''
        self.de_en = 2
        self.filelist = []

    def ui(self):

        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止修改item
        # 初始化列表
        self.show_list(allm)

        # 一旦文字改变便刷新item
        self.lineEdit.textChanged.connect(self.update_list)
        # 处理双击选中item时
        self.listWidget.doubleClicked.connect(self.set_method)
        # 连接start和convert按钮
        self.pushButton.clicked.connect(self.start)

        # 默认方式
        self.encode.setChecked(True)

    def start(self):

        # 获取输入框内的字符串
        self.input()
        self.output()
        # print(self.final)
        # 获取此时的方法
        self.de_en = self.get_de_en()
        # print(self.de_en,self.method)

        # 判断使用什么方法
        self.use_methods()
        # 输出编码后的字符串
        self.output()

    def update_list(self):
        templist = []
        str = self.lineEdit.text()
        for method_name in allm:
            if method_name.find(str) != -1:
                templist.append(method_name)
        self.show_list(templist)

    def set_method(self, qModelIndex):
        self.method = self.listWidget.item(qModelIndex.row()).text()
        self.lineEdit.setText(self.method)

    def show_list(self, list):
        self.listWidget.clear()
        for str in list:
            self.listWidget.addItem(str)

    # 输入与输出
    def input(self):
        self.original = self.input_text_edit.toPlainText()

    def output(self):
        self.output_text_edit.setText(self.final)

    def use_methods(self):

        # 编码encode
        if self.de_en == 2:
            if self.method == '':
                self.final = 'Hey, select a function to decode, stupid!'

                # md5
            elif self.method == 'md5_8':
                self.final = md5_encode_8(self.original)
            elif self.method == 'md5_16':
                self.final = md5_encode_16(self.original)

                # SHA
            elif self.method == 'sha_256':
                self.final = sha_encode_256(self.original)
            elif self.method == 'sha_512':
                self.final = sha_encode_512(self.original)
            elif self.method == 'sha_1':
                self.final = sha_encode_1(self.original)
            elif self.method == 'sha_224':
                self.final = sha_encode_224(self.original)
            elif self.method == 'sha_384':
                self.final = sha_encode_384(self.original)

                # morse code
            elif self.method == 'morse_code':
                self.final = morse_encode(self.original.upper(), '/')

                # base
            elif self.method == 'base64':
                self.final = base64_encode(self.original)
            elif self.method == 'base32':
                self.final = base32_encode(self.original)
            elif self.method == 'base16':
                self.final = base16_encode(self.original)

                # hex
            elif self.method == 'hex':
                self.final = enhex(self.original)
                # else
            else:
                self.final = "Sorry, this method is not supported yet"

        # 解码decode
        elif self.de_en == 1:

            # morse code
            if self.method == 'morse_code':
                self.final = morse_decode(self.original, '/')

                # base
            elif self.method == 'base64':
                self.final = base64_decode(self.original)
            elif self.method == 'base32':
                self.final = base32_decode(self.original)
            elif self.method == 'base16':
                self.final = base16_decode(self.original)

                # hex
            elif self.method == 'hex':
                self.final = dehex(self.original)

                # else
            else:
                self.final = "Sorry, this method is not supported yet"
        else:
            pass

    def get_de_en(self):
        if self.encode.isChecked():
            return 2
        else:
            return 1

    def import_methods(self):
        for filename in os.listdir(os.getcwd()):
            if filename.endswith('py') and filename != '__import__.py':
                self.filelist.append(filename[0:filename.find('.py')])

    # 键盘响应
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.start()


# 主函数main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # 退出app
    sys.exit(app.exec_())
