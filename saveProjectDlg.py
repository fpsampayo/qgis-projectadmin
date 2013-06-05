# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveProjectDlg.ui'
#
# Created: Tue Jul 17 17:29:26 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_saveProjectDlg(object):
    def setupUi(self, saveProjectDlg):
        saveProjectDlg.setObjectName(_fromUtf8("saveProjectDlg"))
        saveProjectDlg.resize(400, 110)
        saveProjectDlg.setMinimumSize(QtCore.QSize(400, 110))
        saveProjectDlg.setMaximumSize(QtCore.QSize(400, 110))
        saveProjectDlg.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(saveProjectDlg)
        self.buttonBox.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(saveProjectDlg)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.campoNombreProyecto = QtGui.QLineEdit(saveProjectDlg)
        self.campoNombreProyecto.setGeometry(QtCore.QRect(180, 30, 211, 21))
        self.campoNombreProyecto.setObjectName(_fromUtf8("campoNombreProyecto"))

        self.retranslateUi(saveProjectDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), saveProjectDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), saveProjectDlg.reject)
        QtCore.QObject.connect(self.campoNombreProyecto, QtCore.SIGNAL(_fromUtf8("returnPressed()")), saveProjectDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(saveProjectDlg)

    def retranslateUi(self, saveProjectDlg):
        saveProjectDlg.setWindowTitle(QtGui.QApplication.translate("saveProjectDlg", "Primer Pluging", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("saveProjectDlg", "Indique el nombre con el que desea guardar el proyecto en la Base de Datos:", None, QtGui.QApplication.UnicodeUTF8))

