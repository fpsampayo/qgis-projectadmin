# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectAdmin_ui.ui'
#
# Created: Fri Jul 27 13:22:37 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_a(object):
    def setupUi(self, a):
        a.setObjectName(_fromUtf8("a"))
        a.setWindowModality(QtCore.Qt.WindowModal)
        a.resize(400, 420)
        a.setMinimumSize(QtCore.QSize(400, 420))
        a.setMaximumSize(QtCore.QSize(400, 420))
        self.buttonBox = QtGui.QDialogButtonBox(a)
        self.buttonBox.setGeometry(QtCore.QRect(230, 380, 161, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabla = QtGui.QTableWidget(a)
        self.tabla.setEnabled(True)
        self.tabla.setGeometry(QtCore.QRect(10, 50, 381, 291))
        self.tabla.setAutoScroll(True)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setTabKeyNavigation(False)
        self.tabla.setAlternatingRowColors(False)
        self.tabla.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setShowGrid(True)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(1)
        self.tabla.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        self.tabla.horizontalHeader().setVisible(True)
        self.tabla.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla.horizontalHeader().setDefaultSectionSize(100)
        self.tabla.horizontalHeader().setHighlightSections(True)
        self.tabla.horizontalHeader().setMinimumSectionSize(35)
        self.tabla.horizontalHeader().setSortIndicatorShown(True)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setMinimumSectionSize(30)
        self.label = QtGui.QLabel(a)
        self.label.setGeometry(QtCore.QRect(10, 20, 331, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnConf = QtGui.QToolButton(a)
        self.btnConf.setGeometry(QtCore.QRect(360, 10, 31, 31))
        self.btnConf.setText(_fromUtf8(""))
        self.btnConf.setIconSize(QtCore.QSize(32, 32))
        self.btnConf.setObjectName(_fromUtf8("btnConf"))
        self.btnSave = QtGui.QToolButton(a)
        self.btnSave.setGeometry(QtCore.QRect(10, 350, 31, 31))
        self.btnSave.setToolTip(_fromUtf8(""))
        self.btnSave.setWhatsThis(_fromUtf8(""))
        self.btnSave.setAccessibleDescription(_fromUtf8(""))
        self.btnSave.setText(_fromUtf8(""))
        self.btnSave.setIconSize(QtCore.QSize(32, 32))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.btnUpdate = QtGui.QToolButton(a)
        self.btnUpdate.setGeometry(QtCore.QRect(50, 350, 31, 31))
        self.btnUpdate.setText(_fromUtf8(""))
        self.btnUpdate.setIconSize(QtCore.QSize(32, 32))
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.btnDelete = QtGui.QToolButton(a)
        self.btnDelete.setGeometry(QtCore.QRect(90, 350, 31, 31))
        self.btnDelete.setText(_fromUtf8(""))
        self.btnDelete.setIconSize(QtCore.QSize(32, 32))
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))

        self.retranslateUi(a)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), a.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), a.reject)
        QtCore.QMetaObject.connectSlotsByName(a)

    def retranslateUi(self, a):
        a.setWindowTitle(QtGui.QApplication.translate("a", "Administrador de Proyectos en PostgreSQL", None, QtGui.QApplication.UnicodeUTF8))
        self.tabla.setSortingEnabled(True)
        self.tabla.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("a", "Nombre Proyecto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("a", "Seleccione un proyecto a cargar o guarde uno nuevo:", None, QtGui.QApplication.UnicodeUTF8))

