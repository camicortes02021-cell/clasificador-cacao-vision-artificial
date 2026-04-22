from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from app.ui.capture_view import CaptureView
from app.ui.results_view import ResultsView
from app.ui.history_view import HistoryView
from app.ui.reports_view import ReportsView
from app.ui.tumaco_info_view import TumacoInfoView
from app.utils.constants import APP_TITLE, BASE_DIR


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.resize(1100, 720)
        self._crear_interfaz()

    def _crear_interfaz(self):
        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        # Fondo de la ventana
        self.fondo_label = QLabel(contenedor)
        self.fondo_label.setScaledContents(True)
        self.fondo_label.lower()  # lo manda al fondo

        fondo_path = BASE_DIR / "assets" / "images" / "fondo_cacao.jpg"
        if fondo_path.exists():
            pixmap = QPixmap(str(fondo_path))
            self.fondo_label.setPixmap(pixmap)
        else:
            print(f"No se encontró la imagen de fondo en: {fondo_path}")

        # Layout principal
        layout = QVBoxLayout(contenedor)
        layout.setContentsMargins(10, 10, 10, 10)

        self.tabs = QTabWidget()
        self.capture_view = CaptureView()
        self.results_view = ResultsView()
        self.history_view = HistoryView()
        self.reports_view = ReportsView()
        self.tumaco_info_view = TumacoInfoView()

        self.capture_view.analisis_completado.connect(self.mostrar_resultados)

        self.tabs.addTab(self.capture_view, "Captura")
        self.tabs.addTab(self.results_view, "Resultados")
        self.tabs.addTab(self.history_view, "Historial")
        self.tabs.addTab(self.reports_view, "Reportes")
        self.tabs.addTab(self.tumaco_info_view, "Cacao de Tumaco")

        layout.addWidget(self.tabs)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "fondo_label"):
            self.fondo_label.setGeometry(0, 0, self.width(), self.height())

    def mostrar_resultados(self, datos, ruta_imagen):
        self.results_view.actualizar_resultado(datos, ruta_imagen)
        self.history_view.cargar_datos()
        self.reports_view.actualizar_grafica()
        self.tabs.setCurrentWidget(self.results_view)
