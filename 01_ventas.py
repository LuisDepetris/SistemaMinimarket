from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic 
from PyQt6.QtGui import QImage, QPixmap


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("tabla.ui", self)      
        self.boton_agregar.clicked.connect(self.agregar)
        self.boton_quitar.clicked.connect(self.eliminar)
        self.boton_editar.clicked.connect(self.editar)
        self.tabla.currentItemChanged.connect(self.seleccionar)
        print(self.tabla.currentRow())

    def editar(self):
        
        # Me traigo los valores de los QLineEdits
        nombre = self.text_nombre.text()
        apellido = self.text_apellido.text()

        # Cambio los elementos en la tabla
        self.tabla.setItem(self.tabla.currentRow(), 0, QTableWidgetItem(nombre))
        self.tabla.setItem(self.tabla.currentRow(), 1, QTableWidgetItem(apellido))

    def seleccionar(self):
        
        # Me traigo los valores seleccionados en la tabla
        nombre_fila = self.tabla.item(self.tabla.currentRow(),0).text()
        apellido_fila = self.tabla.item(self.tabla.currentRow(),1).text()
        
        # Cambio los QlineEdits
        self.text_nombre.setText(nombre_fila)
        self.text_apellido.setText(apellido_fila)

    def agregar(self):
        
        # Creo una fila nueva
        # .setRowCount cambia la cantidad de filas
        # .rowCount() me trae la cantidad de filas

        self.tabla.setRowCount(self.tabla.rowCount()+1)
        
        # Me traigo los datos para insertar la fila
        nombre = self.text_nombre.text()
        apellido = self.text_apellido.text()

        # Inserto los datos en la fila nueva creada
        # .setItem(fila,columna,texto) 6 filas -> 0,1,2,3,4,5

        self.tabla.setItem(self.tabla.rowCount()-1, 0, QTableWidgetItem(nombre))
        self.tabla.setItem(self.tabla.rowCount()-1, 1, QTableWidgetItem(apellido))

        # Limpio los campos
        self.text_nombre.setText("")
        self.text_apellido.setText("")
    
    def eliminar(self):
        # # .currentRow() - Fila actual seleccionada
        fila_actual = self.tabla.currentRow()
        # .removeRow(fila) - Elimina la fila pasada como parámetro
        self.tabla.removeRow(fila_actual)
        # self.tabla.takeItem(self.tabla.currentRow(),self.tabla.currentColumn())


app = QApplication([])
main = Window()

main.show()
app.exec()