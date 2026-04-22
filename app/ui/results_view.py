from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from app.utils.constants import RESULTADOS_COLORES

class ResultsView(QWidget):
    def __init__(self):
        super().__init__()
        self._crear_interfaz()

    def _crear_interfaz(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        titulo = QLabel("Resultado del análisis")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setObjectName("tituloPrincipal")

        self.label_imagen = QLabel("Sin imagen analizada")
        self.label_imagen.setAlignment(Qt.AlignCenter)
        self.label_imagen.setMinimumHeight(250)
        self.label_imagen.setObjectName("panelImagen")

        self.label_resultado = QLabel("Resultado: ---")
        self.label_resultado.setAlignment(Qt.AlignCenter)
        self.label_resultado.setObjectName("resultadoLabel")

        self.label_confianza = QLabel("Confianza: ---")
        self.label_confianza.setAlignment(Qt.AlignCenter)

        self.label_caracteristicas = QLabel("Características: ---")
        self.label_caracteristicas.setAlignment(Qt.AlignCenter)
        self.label_caracteristicas.setWordWrap(True)

        self.label_observacion = QLabel("Observación: ---")
        self.label_observacion.setAlignment(Qt.AlignCenter)
        self.label_observacion.setWordWrap(True)

        caja = QFrame()
        caja_layout = QVBoxLayout(caja)
        caja_layout.addWidget(self.label_resultado)
        caja_layout.addWidget(self.label_confianza)
        caja_layout.addWidget(self.label_caracteristicas)
        caja_layout.addWidget(self.label_observacion)

        layout.addWidget(titulo)
        layout.addWidget(self.label_imagen)
        layout.addWidget(caja)

    def actualizar_resultado(self, datos, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        pixmap_escalado = pixmap.scaled(400, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_imagen.setPixmap(pixmap_escalado)

        resultado = datos["resultado"]
        confianza = datos["confianza"]
        promedio_color = datos["promedio_color"]
        nivel_textura = datos["nivel_textura"]
        observacion = datos["observacion"]

        color = RESULTADOS_COLORES.get(resultado, "#0d6efd")
        self.label_resultado.setText(f"Resultado: {resultado}")
        self.label_resultado.setStyleSheet(f"color: {color}; font-size: 26px; font-weight: bold;")
        self.label_confianza.setText(f"Confianza: {confianza:.1f}%")
        self.label_caracteristicas.setText(f"Promedio de color: {promedio_color:.2f} | Nivel de textura: {nivel_textura:.2f}")
        self.label_observacion.setText(f"Observación: {observacion}")
