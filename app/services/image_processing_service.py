import cv2
import numpy as np
from pathlib import Path

class ImageProcessingService:
    def cargar_imagen(self, ruta_imagen):
        ruta = str(Path(ruta_imagen))

        try:
            datos = np.fromfile(ruta, dtype=np.uint8)
            imagen = cv2.imdecode(datos, cv2.IMREAD_COLOR)
        except Exception:
            imagen = None

        if imagen is None:
            raise ValueError(f"No fue posible cargar la imagen seleccionada: {ruta}")

        return imagen

    def preparar_imagen(self, imagen):
        return cv2.resize(imagen, (224, 224))

    def extraer_caracteristicas(self, imagen):
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        promedio_color = float(np.mean(imagen_rgb))
        desviacion_color = float(np.std(imagen_rgb))
        nivel_textura = float(np.std(imagen_gris))

        return {
            "promedio_color": promedio_color,
            "desviacion_color": desviacion_color,
            "nivel_textura": nivel_textura,
        }
