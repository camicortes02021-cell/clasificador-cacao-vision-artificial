'''from app.services.image_processing_service import ImageProcessingService
from app.services.model_service import ModelService
from app.services.database_service import DatabaseService

class PredictionController:
    def __init__(self):
        self.image_service = ImageProcessingService()
        self.model_service = ModelService()
        self.database_service = DatabaseService()

    def analizar_y_guardar(self, ruta_imagen):
        imagen = self.image_service.cargar_imagen(ruta_imagen)
        imagen_preparada = self.image_service.preparar_imagen(imagen)
        caracteristicas = self.image_service.extraer_caracteristicas(imagen_preparada)
        prediccion = self.model_service.predecir(caracteristicas)

        self.database_service.guardar_evaluacion(
            ruta_imagen=ruta_imagen,
            resultado=prediccion["resultado"],
            confianza=prediccion["confianza"],
            observacion=prediccion["observacion"],
            promedio_color=caracteristicas["promedio_color"],
            nivel_textura=caracteristicas["nivel_textura"],
        )

        return {**prediccion, **caracteristicas}  '''

from pathlib import Path
import numpy as np
import tensorflow as tf

from app.services.image_processing_service import ImageProcessingService
from app.services.database_service import DatabaseService
from app.utils.constants import BASE_DIR

class PredictionController:
    def __init__(self):
        self.image_service = ImageProcessingService()
        self.database_service = DatabaseService()

        modelo_path = BASE_DIR / "ml" / "model" / "cacao_classifier.keras"
        labels_path = BASE_DIR / "ml" / "model" / "labels.txt"

        self.model = tf.keras.models.load_model(modelo_path)

        with open(labels_path, "r", encoding="utf-8") as f:
            self.labels = [line.strip() for line in f.readlines()]

    def analizar_y_guardar(self, ruta_imagen):
        imagen = self.image_service.cargar_imagen(ruta_imagen)
        imagen_preparada = self.image_service.preparar_imagen(imagen)
        caracteristicas = self.image_service.extraer_caracteristicas(imagen_preparada)

        img = imagen_preparada.astype("float32")
        img = np.expand_dims(img, axis=0)

        pred = self.model.predict(img, verbose=0)[0]
        indice = int(np.argmax(pred))
        resultado = self.labels[indice]
        confianza = float(pred[indice] * 100)

        observacion = f"La muestra fue clasificada como {resultado} con base en patrones visuales aprendidos por el modelo."

        self.database_service.guardar_evaluacion(
            ruta_imagen=ruta_imagen,
            resultado=resultado,
            confianza=confianza,
            observacion=observacion,
            promedio_color=caracteristicas["promedio_color"],
            nivel_textura=caracteristicas["nivel_textura"],
        )

        return {
            "resultado": resultado,
            "confianza": confianza,
            "observacion": observacion,
            **caracteristicas,
        }
