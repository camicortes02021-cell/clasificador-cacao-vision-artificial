import cv2

class CameraService:
    def capturar_foto(self, ruta_salida):
        camara = cv2.VideoCapture(0)
        if not camara.isOpened():
            raise RuntimeError("No fue posible acceder a la cámara del equipo.")

        ret, frame = camara.read()
        camara.release()

        if not ret:
            raise RuntimeError("No fue posible capturar la imagen desde la cámara.")

        cv2.imwrite(ruta_salida, frame)
        return ruta_salida
