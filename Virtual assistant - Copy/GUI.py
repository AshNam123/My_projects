# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(812, 461)
        self.label = QtWidgets.QLabel(GUI)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 461))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/projects(python)/Virtual assistant/image/82ab4698e35dbb487566f3cec0503f04.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(GUI)
        self.pushButton.setGeometry(QtCore.QRect(680, 160, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(81, 81, 81);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(GUI)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 200, 93, 28))
        self.pushButton_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(GUI)
        self.textBrowser.setGeometry(QtCore.QRect(250, 10, 121, 31))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(GUI)
        self.textBrowser_2.setGeometry(QtCore.QRect(410, 10, 121, 31))
        self.textBrowser_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "Form"))
        self.pushButton.setText(_translate("GUI", "RUN"))
        self.pushButton_2.setText(_translate("GUI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QWidget()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())
