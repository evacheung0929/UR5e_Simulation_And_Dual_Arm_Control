#!usr/bin/env python3.7.5

# Form implementation generated from reading ui file 'Io_states.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from std_srvs.srv import Trigger, TriggerRequest
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest, IsProgramRunning, IsProgramRunningRequest

from dashboard_dual_service_2 import Dashboard_Client

# class Load_Program_Window(QWidget):
#     '''adds the newly created buttons in vertical direction.'''
#     def setupUi(self, Window2):
#         Window2.setObjectName("Window2")
#         Window2.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(Window2)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(200, 210, 321, 71))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.pushButton.setFont(font)
#         self.pushButton.setIconSize(QtCore.QSize(16, 16))
#         self.pushButton.setObjectName("pushButton")
#         self.toolButton = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton.setGeometry(QtCore.QRect(180, 120, 81, 41))
#         self.toolButton.setObjectName("toolButton")
#         Window2.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(Window2)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
#         self.menubar.setObjectName("menubar")
#         Window2.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(Window2)
#         self.statusbar.setObjectName("statusbar")
#         Window2.setStatusBar(self.statusbar)

#         self.retranslateUi(Window2)
#         QtCore.QMetaObject.connectSlotsByName(Window2)

#     def retranslateUi(self, Window2):
#         _translate = QtCore.QCoreApplication.translate
#         Window2.setWindowTitle(_translate("Window2", "MainWindow"))
#         self.pushButton.setText(_translate("Window2", "Click hehehhehe"))
#         self.toolButton.setText(_translate("Window2", "..."))


# if __name__ == '__main__':        
#     app = QApplication([])
#     load_program = QtWidgets.QMainWindow()
#     ui = Load_Program_Window()
#     ui.setupUi(load_program)
#     ui.show()
#     sys.exec_(app.exec_())

class Load_Program_Window(QWidget):
    '''adds the newly created buttons in vertical direction.'''
    # def setupUi(self, Window2):

    def __init__(self):
        super().__init__()
        # self.window =  QtWidgets.QMainWindow()
        self.layout = QVBoxLayout(self)  # without the self in the QVBoxLayout, cannot see the button!
        self.program_num = 5 # total num of program
        # self.program_button_test()
        self.load_program(robot_name='')

    def program_button_test(self, program_name):
        # program_name = {'test':'external_test', 'external':'external_control'}
        for i in program_name:
            button = QPushButton(program_name[i],clicked = lambda: print('hey')) # 
            self.layout.addWidget(button)

    def load(self, robot_name, file_name):
        '''Basic example of how load program is implemented without integrating it into UI'''
        if robot_name.lower() =='p':
            programe_name = {'external':'external_control'}
        elif robot_name.lower() =='d':
            programe_name = {'external':'external_control'}
        elif robot_name =='':
            programe_name={'test':'external_test', 'external':'external_control'}
        
        load_prog = Dashboard_Client('load_program', Load, LoadRequest())
        load_prog.load(file_name = programe_name[file_name])
    
    def load_program(self, robot_name):
        '''this function generate a list of buttons corresponding to the amount of '''
        if robot_name.lower() =='p':
            programe_name = {'external':'external_control'}
        elif robot_name.lower() =='d':
            programe_name = {'external':'external_control'}
        elif robot_name =='':
            programe_name={'test':'external_test', 'external':'external_control'}
        
        for i in programe_name:
            # load_prog = Dashboard_Client('load_program', Load, LoadRequest(),'')
            # l = load_prog.load(programe_name[i])
            button = QPushButton(programe_name[i] ) # clicked = (lambda x: print(programe_name[i]))
            button.clicked.connect(lambda b, i=i:print(f"{programe_name[i]} program has been selected"))
            # button.clicked.connect(lambda b, i=i:l)
            self.layout.addWidget(button)

if __name__ == '__main__':        

    # Create the Qt application
    app = QApplication([])

    load_program = Load_Program_Window()
    load_program.show()
    app.exec_()