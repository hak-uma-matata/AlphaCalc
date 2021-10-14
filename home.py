# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as ms
from pathlib import Path
from calculator import Ui_CalcWindow

def relative_to_bg(path: str) -> Path:
        return BG_PATH / Path(path)
OUTPUT_PATH = Path(__file__).parent
BG_PATH = OUTPUT_PATH / Path("./backgrounds")

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(500, 654)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 500, 654))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap(str(relative_to_bg("bg.jpg"))))
        self.bg.setObjectName("bg")
        self.hide = QtWidgets.QLabel(self.centralwidget)
        self.hide.setGeometry(QtCore.QRect(20, 600, 461, 31))
        self.hide.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.hide.setText("")
        self.hide.setObjectName("hide")
        self.pwd_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_input.setGeometry(QtCore.QRect(247, 473, 231, 28))
        self.pwd_input.setStyleSheet("background-color: rgb(255, 131, 133);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pwd_input.setText("")
        self.pwd_input.setFrame(False)
        self.pwd_input.setObjectName("pwd_input")
        self.pwd_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.submit = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.login())
        self.submit.setGeometry(QtCore.QRect(185, 535, 135, 45))
        self.submit.setStyleSheet("background-color: rgb(255, 67, 70);\n"
"font: 20pt \"Franklin Gothic Demi Cond\";")
        self.submit.setAutoDefault(False)
        self.submit.setFlat(False)
        self.submit.setObjectName("submit")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "AlphaCalc"))
        self.submit.setText(_translate("LoginWindow", "Submit"))

    def login(self):
        try:
            ms.connect(host = "localhost", user = "root", passwd = self.pwd_input.text())
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_CalcWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            LoginWindow.hide()
        except Exception:
            self.hide.setHidden(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
