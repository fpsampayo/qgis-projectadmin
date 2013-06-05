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
from ProjectAdmin_ui import Ui_a
# create the dialog for zoom to point
class ProjectAdminDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_a()
        self.ui.setupUi(self)
