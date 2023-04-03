# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Io_states.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

class Load_Program_Window(QWidget):
    '''adds the newly created buttons in vertical direction.'''
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 210, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(180, 120, 81, 41))
        self.toolButton.setObjectName("toolButton")
        Window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Window2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window2)
        self.statusbar.setObjectName("statusbar")
        Window2.setStatusBar(self.statusbar)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "MainWindow"))
        self.pushButton.setText(_translate("Window2", "Click hehehhehe"))
        self.toolButton.setText(_translate("Window2", "..."))


if __name__ == '__main__':        
    app = QApplication([])
    load_program = QtWidgets.QMainWindow()
    ui = Load_Program_Window()
    # mainapp.show()
    ui.setupUi(load_program)
    ui.show()
    sys.exec_(app.exec_())

    # def __init__(self):
    #     super().__init__()
    #     self.window =  QWidget()
    #     self.layout = QVBoxLayout() 
    #     self.program_list()
    #     self.program_num = 5 # total num of program

    # def program_list(self):
    #     self.layout.addWidget(QPushButton('1'))
    #     # for i in range(8):
    #     #     button = self.layout.addWidget(QPushButton('Name list'))
    #     #     # button.clicked.connect(lambda ch, i=i: self.function(i))
    #     self.window.setLayout(self.layout)
    #     self.window.show()

# if __name__ == '__main__':        
#     app = QApplication([])
#     mainapp = QWidget()
#     # mainapp.show()
#     app.exec_()

