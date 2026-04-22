from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from app.controllers.history_controller import HistoryController

class ReportsView(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = HistoryController()
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        self._crear_interfaz()
        self.actualizar_grafica()

    def _crear_interfaz(self):
        layout = QVBoxLayout(self)

        titulo = QLabel("Reporte gráfico de evaluaciones")
        titulo.setObjectName("tituloPrincipal")

        self.btn_actualizar = QPushButton("Actualizar reporte")
        self.btn_actualizar.clicked.connect(self.actualizar_grafica)

        layout.addWidget(titulo)
        layout.addWidget(self.canvas)
        layout.addWidget(self.btn_actualizar)

    def actualizar_grafica(self):
        datos = self.controller.obtener_resumen()
        etiquetas = [fila[0] for fila in datos]
        cantidades = [fila[1] for fila in datos]

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if etiquetas:
            ax.bar(etiquetas, cantidades)
            ax.set_title("Cantidad de muestras por categoría")
            ax.set_xlabel("Calidad")
            ax.set_ylabel("Cantidad")
        else:
            ax.text(0.5, 0.5, "Aún no hay registros.", ha="center", va="center")
            ax.set_axis_off()

        self.canvas.draw()
