# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confDlg.ui'
#
# Created: Tue Jul 24 12:34:51 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_confDlg(object):
    def setupUi(self, confDlg):
        confDlg.setObjectName(_fromUtf8("confDlg"))
        confDlg.resize(247, 200)
        confDlg.setMinimumSize(QtCore.QSize(240, 140))
        confDlg.setMaximumSize(QtCore.QSize(400, 200))
        confDlg.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(confDlg)
        self.buttonBox.setGeometry(QtCore.QRect(10, 160, 221, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.campoHost = QtGui.QLineEdit(confDlg)
        self.campoHost.setGeometry(QtCore.QRect(100, 10, 131, 21))
        self.campoHost.setAccessibleName(_fromUtf8(""))
        self.campoHost.setAccessibleDescription(_fromUtf8(""))
        self.campoHost.setInputMask(_fromUtf8(""))
        self.campoHost.setText(_fromUtf8(""))
        self.campoHost.setObjectName(_fromUtf8("campoHost"))
        self.label = QtGui.QLabel(confDlg)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(confDlg)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(confDlg)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.campoPort = QtGui.QLineEdit(confDlg)
        self.campoPort.setGeometry(QtCore.QRect(100, 40, 131, 21))
        self.campoPort.setAccessibleName(_fromUtf8(""))
        self.campoPort.setAccessibleDescription(_fromUtf8(""))
        self.campoPort.setInputMask(_fromUtf8(""))
        self.campoPort.setText(_fromUtf8(""))
        self.campoPort.setObjectName(_fromUtf8("campoPort"))
        self.campoDDBB = QtGui.QLineEdit(confDlg)
        self.campoDDBB.setGeometry(QtCore.QRect(100, 70, 131, 21))
        self.campoDDBB.setAccessibleName(_fromUtf8(""))
        self.campoDDBB.setAccessibleDescription(_fromUtf8(""))
        self.campoDDBB.setInputMask(_fromUtf8(""))
        self.campoDDBB.setText(_fromUtf8(""))
        self.campoDDBB.setObjectName(_fromUtf8("campoDDBB"))
        self.campoUser = QtGui.QLineEdit(confDlg)
        self.campoUser.setGeometry(QtCore.QRect(100, 100, 131, 21))
        self.campoUser.setAccessibleName(_fromUtf8(""))
        self.campoUser.setAccessibleDescription(_fromUtf8(""))
        self.campoUser.setInputMask(_fromUtf8(""))
        self.campoUser.setText(_fromUtf8(""))
        self.campoUser.setObjectName(_fromUtf8("campoUser"))
        self.label_4 = QtGui.QLabel(confDlg)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.campoPass = QtGui.QLineEdit(confDlg)
        self.campoPass.setGeometry(QtCore.QRect(100, 130, 131, 20))
        self.campoPass.setEchoMode(QtGui.QLineEdit.Password)
        self.campoPass.setObjectName(_fromUtf8("campoPass"))
        self.label_5 = QtGui.QLabel(confDlg)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(confDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), confDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), confDlg.reject)
        QtCore.QObject.connect(self.campoHost, QtCore.SIGNAL(_fromUtf8("returnPressed()")), confDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(confDlg)

    def retranslateUi(self, confDlg):
        confDlg.setWindowTitle(QtGui.QApplication.translate("confDlg", "Primer Pluging", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("confDlg", "Servidor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("confDlg", "Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("confDlg", "Base de Datos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("confDlg", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("confDlg", "Contraseña:", None, QtGui.QApplication.UnicodeUTF8))

