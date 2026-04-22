from datetime import datetime
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from app.controllers.prediction_controller import PredictionController
from app.services.camera_service import CameraService
from app.utils.constants import IMAGES_DIR

class CaptureView(QWidget):
    analisis_completado = Signal(dict, str)

    def __init__(self):
        super().__init__()
        self.ruta_imagen_actual = None
        self.prediction_controller = PredictionController()
        self.camera_service = CameraService()
        self._crear_interfaz()

    def _crear_interfaz(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setSpacing(15)

        titulo = QLabel("Captura y análisis de muestras de cacao")
        titulo.setObjectName("tituloPrincipal")
        titulo.setAlignment(Qt.AlignCenter)

        self.label_imagen = QLabel("Aquí se mostrará la imagen seleccionada")
        self.label_imagen.setAlignment(Qt.AlignCenter)
        self.label_imagen.setMinimumHeight(320)
        self.label_imagen.setObjectName("panelImagen")

        layout_botones = QHBoxLayout()
        self.btn_cargar = QPushButton("Cargar imagen")
        self.btn_camara = QPushButton("Usar cámara")
        self.btn_analizar = QPushButton("Analizar muestra")

        self.btn_cargar.clicked.connect(self.cargar_imagen)
        self.btn_camara.clicked.connect(self.capturar_desde_camara)
        self.btn_analizar.clicked.connect(self.analizar_imagen)

        layout_botones.addWidget(self.btn_cargar)
        layout_botones.addWidget(self.btn_camara)
        layout_botones.addWidget(self.btn_analizar)

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(self.label_imagen)
        layout_principal.addLayout(layout_botones)

    def cargar_imagen(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp)")
        if ruta_archivo:
            self.ruta_imagen_actual = ruta_archivo
            self._mostrar_imagen(ruta_archivo)

    def capturar_desde_camara(self):
        try:
            nombre_archivo = f"captura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            ruta_salida = IMAGES_DIR / nombre_archivo
            ruta_final = self.camera_service.capturar_foto(str(ruta_salida))
            self.ruta_imagen_actual = ruta_final
            self._mostrar_imagen(ruta_final)
            QMessageBox.information(self, "Captura exitosa", "La imagen fue tomada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error de cámara", str(e))

    def analizar_imagen(self):
        if not self.ruta_imagen_actual:
            QMessageBox.warning(self, "Falta imagen", "Primero debes cargar una imagen o tomar una foto.")
            return

        try:
            resultado = self.prediction_controller.analizar_y_guardar(self.ruta_imagen_actual)
            self.analisis_completado.emit(resultado, self.ruta_imagen_actual)
            QMessageBox.information(self, "Proceso completado", "La muestra fue analizada y guardada.")
        except Exception as e:
            QMessageBox.critical(self, "Error de análisis", str(e))

    def _mostrar_imagen(self, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        pixmap_escalado = pixmap.scaled(500, 320, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_imagen.setPixmap(pixmap_escalado)
