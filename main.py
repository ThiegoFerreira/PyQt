from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from login import Ui_login
from tela import Ui_MainWindow
from cadastro import Ui_cadastro



class cadastro(QDialog):
    def __init__(self,*args,**argvs):
        super(cadastro,self).__init__(*args,**argvs)
        self.ui = Ui_cadastro()
        self.ui.setupUi(self)

class telaprincipal(QMainWindow):
    def __init__(self,*args,**argvs):
        super(telaprincipal,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.add)

    def add(self):
        add = cadastro()
        add.exec_()

class login(QDialog):
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.login)
    
    def login(self):
        admin = "admin"
        senha = "admin"

        user = self.ui.lineEdit.text()
        passd = self.ui.lineEdit_2.text()

        if user == admin and passd == senha:
            QMessageBox.information(QMessageBox(),"login realizado!", "Acesso Autorizado!")
            self.window = telaprincipal()
            self.window.show()
        
        else:
            QMessageBox.warning(QMessageBox(),"login não realizado!", "Acesso Negado!")



app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = login()
    window.show()
sys.exit(app.exec_())