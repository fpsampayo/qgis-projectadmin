# -*- coding: utf-8 -*-
"""
/***************************************************************************
 aDialog
                                 A QGIS plugin
 a
                             -------------------
        begin                : 2012-07-12
        copyright            : (C) 2012 by a
        email                : a
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from saveProjectDlg import Ui_saveProjectDlg
# create the dialog for zoom to point
class saveProjectDlgWindowDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_saveProjectDlg()
        self.ui.setupUi(self)
