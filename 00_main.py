from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox
from PyQt6 import uic 
from PyQt6.QtGui import QImage, QPixmap
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__),"main.ui"), self)
        self.ventana_proveedores = ventanaProveedores(self)
        self.cmd_appcaja.clicked.connect(self.onClickAppCaja)
        self.cmd_ventas.clicked.connect(self.onClickVentas)
        self.cmd_productos.clicked.connect(self.onClickProductos)
        self.cmd_proveedores.clicked.connect(self.onClickProveedores)
        self.cmd_configuracion.clicked.connect(self.onClickedConfiguracion)
        self.cmd_salir.clicked.connect(self.onClickedSalir)
        
    def onClickAppCaja(self):
        pass

    def onClickVentas(self):
        self.lbl_icono.setPixmap(QPixmap.fromImage(QImage("pictures/punto-de-venta.png")))
        self.lbl_prueba.setText("AQUI ABRO LA VENTANA DE VENTAS")
    
    def onClickProductos(self):
        self.lbl_icono.setPixmap(QPixmap.fromImage(QImage("pictures/paquete.png")))
        self.lbl_prueba.setText("AQUI ABRO LA VENTANA DE PRODUCTOS")

    def onClickProveedores(self):
        self.ventana_proveedores.show()

    def onClickedConfiguracion(self):
        self.lbl_icono.setPixmap(QPixmap.fromImage(QImage("pictures/configuraciones.png")))
        self.lbl_prueba.setText("AQUI ABRO LA VENTANA DE CONFIGURACION")

    def onClickedSalir(self):
        self.close()

class ventanaAperturaCaja(QMainWindow):
    pass

class ventanaVentas(QMainWindow):
    pass

class ventanaProductos(QMainWindow):
    pass

class ventanaProveedores(QMainWindow):
    def __init__(self, mainWindows):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__),"proveedores.ui"),self)
        self.mainWindows = mainWindows
        self.cmd_add.clicked.connect(self.onClickAdd)
        self.cmd_edit.clicked.connect(self.onClickEdit)
        self.cmd_delete.clicked.connect(self.onClickDelete)
        self.cmd_exit.clicked.connect(self.onClickExit)
        self.grid.currentItemChanged.connect(self.seleccionar)
    
    def seleccionar(self):
        id = self.grid.item(self.grid.currentRow(),0).text()
        nombre = self.grid.item(self.grid.currentRow(),1).text()
        telefono = self.grid.item(self.grid.currentRow(),2).text()
        direccion = self.grid.item(self.grid.currentRow(),3).text()
        saldos = self.grid.item(self.grid.currentRow(),4).text()
        
        self.txt_id.setText(id)
        self.txt_nombre.setText(nombre)
        self.txt_telefono.setText(telefono)
        self.txt_direccion.setText(direccion)
        self.txt_saldo.setText(saldos)

    def onClickAdd(self):
        #agregar una fila nueva
        self.grid.setRowCount(self.grid.rowCount()+1)

        #Tomar los datos del proveedor
        id = self.txt_id.text()
        nombre = self.txt_nombre.text()
        telefono = self.txt_telefono.text()
        direccion = self.txt_direccion.text()
        saldos = self.txt_saldo.text()

        #Agregar el item en el grid
        self.grid.setItem(self.grid.rowCount()-1, 0, QTableWidgetItem(id))
        self.grid.setItem(self.grid.rowCount()-1, 1, QTableWidgetItem(nombre))
        self.grid.setItem(self.grid.rowCount()-1, 2, QTableWidgetItem(telefono))
        self.grid.setItem(self.grid.rowCount()-1, 3, QTableWidgetItem(direccion))
        self.grid.setItem(self.grid.rowCount()-1, 4, QTableWidgetItem(saldos))

        #Limpiar los texts box
        self.txt_id.setText("")
        self.txt_nombre.setText("")
        self.txt_telefono.setText("")
        self.txt_direccion.setText("")
        self.txt_saldo.setText("")

    def onClickEdit(self):
        item = self.grid.currentItem()
        if (item == None):
            return
        
        #Tomar los datos del proveedor
        id = self.txt_id.text()
        nombre = self.txt_nombre.text()
        telefono = self.txt_telefono.text()
        direccion = self.txt_direccion.text()
        saldos = self.txt_saldo.text()

        self.grid.setItem(self.grid.currentRow(), 0, QTableWidgetItem(id))
        self.grid.setItem(self.grid.currentRow(), 1, QTableWidgetItem(nombre))
        self.grid.setItem(self.grid.currentRow(), 2, QTableWidgetItem(telefono))
        self.grid.setItem(self.grid.currentRow(), 3, QTableWidgetItem(direccion))
        self.grid.setItem(self.grid.currentRow(), 4, QTableWidgetItem(saldos))

    def onClickDelete(self):
        fila_eliminar = self.grid.currentItem()
        if (fila_eliminar == None):
            return
        mensaje = QMessageBox()

        mensaje.setWindowTitle('Eliminar fila')
        mensaje.setText('¿Desea eliminar fila?')
        mensaje.setIcon(QMessageBox.Icon.Warning)
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        resultado = mensaje.exec()
        if (resultado == QMessageBox.StandardButton.Yes):
        # Quitar fila
            fila = fila_eliminar.row()
            self.grid.removeRow(fila)
    
    def onClickExit(self):
        self.close()
        self.mainWindows.show()


app = QApplication([])
main = Window()

main.show()
app.exec()