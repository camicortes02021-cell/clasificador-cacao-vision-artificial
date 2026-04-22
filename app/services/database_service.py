import sqlite3
from datetime import datetime
from app.utils.constants import DATABASE_PATH

class DatabaseService:
    def __init__(self):
        self.db_path = str(DATABASE_PATH)
        self._crear_tablas()

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _crear_tablas(self):
        conexion = self._conectar()
        cursor = conexion.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS evaluaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                ruta_imagen TEXT NOT NULL,
                resultado TEXT NOT NULL,
                confianza REAL NOT NULL,
                observacion TEXT,
                promedio_color REAL,
                nivel_textura REAL
            )
            '''
        )
        conexion.commit()
        conexion.close()

    def guardar_evaluacion(self, ruta_imagen, resultado, confianza, observacion, promedio_color, nivel_textura):
        conexion = self._conectar()
        cursor = conexion.cursor()
        cursor.execute(
            '''
            INSERT INTO evaluaciones (
                fecha, ruta_imagen, resultado, confianza, observacion, promedio_color, nivel_textura
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ruta_imagen,
                resultado,
                float(confianza),
                observacion,
                float(promedio_color),
                float(nivel_textura),
            )
        )
        conexion.commit()
        conexion.close()

    def obtener_historial(self):
        conexion = self._conectar()
        cursor = conexion.cursor()
        cursor.execute(
            '''
            SELECT id, fecha, ruta_imagen, resultado, confianza, observacion
            FROM evaluaciones
            ORDER BY id DESC
            '''
        )
        filas = cursor.fetchall()
        conexion.close()
        return filas

    def obtener_resumen_resultados(self):
        conexion = self._conectar()
        cursor = conexion.cursor()
        cursor.execute(
            '''
            SELECT resultado, COUNT(*) as cantidad
            FROM evaluaciones
            GROUP BY resultado
            '''
        )
        filas = cursor.fetchall()
        conexion.close()
        return filas
