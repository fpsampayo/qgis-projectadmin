# -*- coding: utf8 -*- 
"""
/***************************************************************************
 a
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import qgis.utils
import psycopg2
import tempfile
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from ProjectAdminDialog import ProjectAdminDialog
from saveProjectDlgDialog import saveProjectDlgWindowDialog
from confDlgDialog import confDlgWindowDialog
from PyQt4 import QtGui, Qt
import PyQt4
from ProjectAdmin_ui import _fromUtf8

class ProjectAdmin:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # Create the dialog and keep reference
        self.dlg = ProjectAdminDialog()
        self.dlg_save = saveProjectDlgWindowDialog()
        self.dlg_conf = confDlgWindowDialog()
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/ProjectAdmin"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
        
        
        self.settings = QSettings("fpsampayo", "administradorProyectos")
        self.host = self.settings.value("host")
        self.port = self.settings.value("port")
        self.ddbb = self.settings.value("ddbb")
        self.user = self.settings.value("user")
        self.passwd = self.settings.value("passwd")
                
        
       
        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/ProjectAdmin_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
   
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/ProjectAdmin/icon.png"), \
            u"ProjectAdmin", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
                   
        QObject.connect(self.dlg.ui.btnSave, SIGNAL("clicked()"), self.saveProjectAction)
        QObject.connect(self.dlg.ui.btnConf, SIGNAL("clicked()"), self.confDialogAction)
        QObject.connect(self.dlg.ui.btnDelete, SIGNAL("clicked()"), self.deleteProjectAction)
        QObject.connect(self.dlg.ui.btnUpdate, SIGNAL("clicked()"), self.updateProjectAction)
        
        icon_conf = QtGui.QIcon()
        icon_conf.addPixmap(QtGui.QPixmap(_fromUtf8(":plugins/ProjectAdmin/conf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dlg.ui.btnConf.setIcon(icon_conf)
        self.dlg.ui.btnConf.setToolTip(u"Configuración de conexión")
        
        icon_save_new = QtGui.QIcon()
        icon_save_new.addPixmap(QtGui.QPixmap(_fromUtf8(":plugins/ProjectAdmin/save_new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dlg.ui.btnSave.setIcon(icon_save_new)
        self.dlg.ui.btnSave.setToolTip("Guardar nuevo proyecto")
        
        icon_save = QtGui.QIcon()
        icon_save.addPixmap(QtGui.QPixmap(_fromUtf8(":plugins/ProjectAdmin/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dlg.ui.btnUpdate.setIcon(icon_save)
        self.dlg.ui.btnUpdate.setToolTip("Actualizar proyecto seleccionado")
        
        icon_del = QtGui.QIcon()
        icon_del.addPixmap(QtGui.QPixmap(_fromUtf8(":plugins/ProjectAdmin/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dlg.ui.btnDelete.setIcon(icon_del)
        self.dlg.ui.btnDelete.setToolTip("Emiminar proyecto seleccionado")
        
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&ProjectAdmin", self.action)
        
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&ProjectAdmin",self.action)
        self.iface.removeToolBarIcon(self.action)
        
    # run method that performs all the real work
    
    def run(self):
        # show the dialog
        self.dlg.show()
        self.leerProyectos()
        # Run the dialog event loop
        result = self.dlg.exec_()
        
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            if len(self.dlg.ui.tabla.selectedItems()) == 0:
                QMessageBox.information(None, "Aviso", u"Debe seleccionar algún proyecto de la tabla.")
                self.run()
            else:
                QMessageBox.information(None, "Aviso", "Has seleccionado el proyecto " + str(self.dlg.ui.tabla.selectedItems()[0].text()))
                self.loadProject(str(self.dlg.ui.tabla.selectedItems()[0].text()))
                                    
    def saveProject(self, nombre_proyecto):

        self.conectarDDBB()
        temp_file = tempfile.NamedTemporaryFile('w+b', -1, ".qgs", tempfile.gettempprefix(), tempfile.gettempdir(), False)

        qstr = QString(temp_file.name)
        
        project = QgsProject.instance()
        try:
            project.setFileName(qstr)
            project.write()
        except:
            QMessageBox.Information(None, "Aviso", "Falló el guardado del fichero temporal.")
        
        fp = open(temp_file.name)
        if self.projectExist(nombre_proyecto):
            self.cur.execute("UPDATE proyectos SET proyecto=%s WHERE nombre=%s", (fp.read(), str(nombre_proyecto)))
        else:
            self.cur.execute("INSERT INTO proyectos (proyecto, nombre) VALUES (%s, %s)", (fp.read(), str(nombre_proyecto)))
        self.conn.commit()
        self.desconectarDDBB()

        temp_file.close()
        self.leerProyectos()
        
    def deleteProject(self, nombre):
        
        self.conectarDDBB()
        try:
            self.cur.execute("DELETE FROM proyectos WHERE nombre LIKE '" + nombre + "'")
            self.conn.commit()
        except:
            QMessageBox.Information(None, "Error", "Falló el borrado del proyecto '" + nombre + "'.")
        self.desconectarDDBB()
        self.leerProyectos()
        
    def updateProject(self, nombre):
        
        self.conectarDDBB()
        try:
            self.cur.execute("UPDATE proyectos SET proyecto=" + nombre + "'")
            self.conn.commit()
        except:
            QMessageBox.Information(None, "Error", "Falló al altualizar el proyecto '" + nombre + "'.")
        
        self.desconectarDDBB()
        
    def loadProject(self, nombre):
      
        cur = self.conectarDDBB()
        cur.execute("SELECT proyecto FROM proyectos WHERE nombre LIKE '" + nombre + "'")
        contenido_fichero = cur.fetchall()
        
        #print "Ejecutando: " + "\"SELECT proyecto FROM proyectos WHERE nombre LIKE '" + nombre + "'\""
        #print str(contenido_fichero[0][0])
        
        temp_file = tempfile.NamedTemporaryFile('w+b', -1, ".qgs", nombre + "-" + tempfile.gettempprefix(), tempfile.gettempdir(), False)
        temp_file.write(str(contenido_fichero[0][0]))
        temp_file.seek(0)
        
        qstr = QString(temp_file.name)
        
        #print temp_file.name
        #print qstr
        
        self.iface.addProject(qstr)
        
        temp_file.close()
        
        self.desconectarDDBB()
    
    def leerProyectos(self):
        """Función encargada de leer la DDBB para buscar proyectos guardados
        en ella al inicio del pluging y rellenar con estos la QTable"""

        try:
            cur = self.conectarDDBB()
            cur.execute("SELECT nombre FROM proyectos")
            proyectos = cur.fetchall()
            self.dlg.ui.tabla.setRowCount(len(proyectos))
            numFilas = 0
            for project in proyectos:
                project_name = project[0]
                valor1 = QtGui.QTableWidgetItem()
                valor1.setText(str(project_name))
                self.dlg.ui.tabla.setItem(numFilas, 0, valor1)
    
                numFilas = numFilas + 1
                
            self.desconectarDDBB()
        except:
            pass
        
    def comprobarCapas(self):
        """Comprueba que las capas del proyecto sean de tipo PostGIS o WMS ya que el resto de capas no tienen soporte 
        dado que pueden tenerse en local."""
        
        layers = self.iface.legendInterface().layers()
        result = True
        
        for layer in layers:
            layerType = layer.type()
            if layerType == QgsMapLayer.VectorLayer:
                #layerName = layer.name()
                #layerSource = layer.source()
                pt = layer.providerType()
                if pt == "ogr":
                    storage = str(layer.storageType())
                    if storage != "PostgreSQL":
                        #QMessageBox.information(None, "Aviso", 
                        #u"Solo las capas WMS y PostGIS están soportadas.")
                        result = False
            elif layerType == QgsMapLayer.RasterLayer:
                pt = layer.providerType()
                if pt != "wms":
                    result = False
            else:
                result = False
        
        return result
        
    def projectExist(self, nombre):
        """Comprueba si el nombre dado al nuevo proyecto ya existe en la DDBB"""

        cur = self.conectarDDBB()
        cur.execute("SELECT nombre FROM proyectos")
        nombres_proyectos = cur.fetchall()
        #print "[projectExist]: nombre_nuevo_proyecto = " + str(nombre)
        
        for nombre_proyecto_db in nombres_proyectos:
            for valor in nombre_proyecto_db:
                #print "[projectExist]: nombre_proyecto_db = " + str(valor)
                if nombre == str(valor):
                    return True
                else:
                    return False

        self.desconectarDDBB()
    
    def saveProjectAction(self):
        self.dlg.close()
        self.dlg_save.show()
        result = self.dlg_save.exec_()
        if result == 1:
            if self.projectExist(self.dlg_save.ui.campoNombreProyecto.text()):
                QMessageBox.information(None, "Aviso", 
                    u"El nombre indicado ya existe en Base de Datos.")
            elif self.comprobarCapas() == False:
                QMessageBox.information(None, "Aviso", u"Sólo las capas PostGIS y WMS están soportadas")
            else:
                self.saveProject(self.dlg_save.ui.campoNombreProyecto.text())
                QMessageBox.information(None, "Aviso", "El proyecto \"" + str(self.dlg_save.ui.campoNombreProyecto.text()) + "\" se ha guardado correctamente en Base de Datos")
                self.dlg.show()
                
    def deleteProjectAction(self):
        """while len(self.dlg.ui.tabla.selectedItems()) == 0:
            self.dlg.ui.btnDelete.setDisabled(True)
        """
        
        if len(self.dlg.ui.tabla.selectedItems()) == 0:
            QMessageBox.information(None, "Aviso", u"Debe seleccionar algún proyecto de la tabla.")
            self.run()
        elif QMessageBox.question(None, u"Actualización de Proyecto", u"Está seguro de que desea borrar el proyecto '" + str(self.dlg.ui.tabla.selectedItems()[0].text()) + "'?", buttons=QMessageBox.Ok, defaultButton=QMessageBox.Cancel) == QMessageBox.Ok:            
            nombre = str(self.dlg.ui.tabla.selectedItems()[0].text())
            self.deleteProject(nombre)
            QMessageBox.information(None, "Aviso", "Se ha eliminado el proyecto '" + nombre + "'.")
            
    def updateProjectAction(self):
        
        if len(self.dlg.ui.tabla.selectedItems()) == 0:
            QMessageBox.information(None, "Aviso", u"Debe seleccionar algún proyecto de la tabla.")
            self.run()
        elif self.comprobarCapas() == False:
                QMessageBox.information(None, "Aviso", u"Sólo las capas PostGIS y WMS están soportadas")    
        else:            
            if QMessageBox.question(None, u"Actualización de Proyecto", u"Está seguro de que desea sobreescribir el proyecto seleccionado?", buttons=QMessageBox.Ok, defaultButton=QMessageBox.Cancel) == QMessageBox.Ok :
                    self.saveProject((str(self.dlg.ui.tabla.selectedItems()[0].text())))
                    QMessageBox.information(None, "Aviso", "Se ha actualizado el proyecto '" + str(self.dlg.ui.tabla.selectedItems()[0].text()) + "'.")
                                                           
    def confDialogAction(self):
        
        #settings = QSettings("fpsampayo", "administradorProyectos")
        self.host = self.settings.value("host")
        self.port = self.settings.value("port")
        self.ddbb = self.settings.value("ddbb")
        self.user = self.settings.value("user")
        self.passwd = self.settings.value("passwd")
        
        
        self.dlg_conf.show()
        self.dlg_conf.ui.campoHost.setText(self.host.toString())
        self.dlg_conf.ui.campoPort.setText(self.port.toString())
        self.dlg_conf.ui.campoDDBB.setText(self.ddbb.toString())
        self.dlg_conf.ui.campoUser.setText(self.user.toString())
        self.dlg_conf.ui.campoPass.setText(self.passwd.toString())
        
        result = self.dlg_conf.exec_()
        
        if result == 1:
            self.settings.setValue("host", QVariant(self.dlg_conf.ui.campoHost.text()))
            self.settings.setValue("port", QVariant(self.dlg_conf.ui.campoPort.text()))
            self.settings.setValue("ddbb", QVariant(self.dlg_conf.ui.campoDDBB.text()))
            self.settings.setValue("user", QVariant(self.dlg_conf.ui.campoUser.text()))
            self.settings.setValue("passwd", QVariant(self.dlg_conf.ui.campoPass.text()))
        
    def conectarDDBB(self):
        
        try:
            self.conn = psycopg2.connect("dbname='" + str(self.ddbb.toString()) + "' user='" + str(self.user.toString()) + "' host='" + str(self.host.toString()) + "' port='" + str(self.port.toString()) + "' password='" + str(self.passwd.toString()) + "'")
            self.cur = self.conn.cursor()
            return self.cur
        except:
            QMessageBox.information(None, "Aviso", u"La conexión ha sido errónea. \nVerifique los datos de conexión.")
            self.confDialogAction()
            pass   
    
    def desconectarDDBB(self):
        
        self.cur.close()
        self.conn.close()
        
        
        
            