# -*- coding: utf-8 -*-
"""
/***************************************************************************
 a
                                 A QGIS plugin
 a
                             -------------------
        begin                : 2012-07-12
        copyright            : (C) 2012 by fpsampayo
        email                : fpsampayo@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "ProjectAdmin"
def description():
    return "Plugin para guardar proyectos dentro de PostgreSQL"
def version():
    return "Version 0.1"
def icon():
    return "./icon/icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load a class from file a
    from ProjectAdmin import ProjectAdmin
    return ProjectAdmin(iface)
