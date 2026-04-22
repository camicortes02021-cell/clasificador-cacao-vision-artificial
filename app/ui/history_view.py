from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from app.controllers.history_controller import HistoryController

class HistoryView(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = HistoryController()
        self._crear_interfaz()
        self.cargar_datos()

    def _crear_interfaz(self):
        layout = QVBoxLayout(self)

        titulo = QLabel("Historial de evaluaciones")
        titulo.setObjectName("tituloPrincipal")

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["ID", "Fecha", "Ruta imagen", "Resultado", "Confianza", "Observación"])
        self.tabla.horizontalHeader().setStretchLastSection(True)

        self.btn_actualizar = QPushButton("Actualizar historial")
        self.btn_actualizar.clicked.connect(self.cargar_datos)

        layout.addWidget(titulo)
        layout.addWidget(self.tabla)
        layout.addWidget(self.btn_actualizar)

    def cargar_datos(self):
        registros = self.controller.obtener_historial()
        self.tabla.setRowCount(len(registros))

        for fila, registro in enumerate(registros):
            for columna, valor in enumerate(registro):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))
