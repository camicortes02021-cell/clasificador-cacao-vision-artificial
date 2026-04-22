from pathlib import Path

#BASE_DIR = Path(__file__).resolve().parents[2]
#DATABASE_PATH = BASE_DIR / "data" / "database" / "cacao.db"
#IMAGES_DIR = BASE_DIR / "data" / "images"
#APP_TITLE = "Clasificador de Calidad de Cacao con IA"

#RESULTADOS_COLORES = {
    #"Bueno": "#198754",
    #"Regular": "#ffc107",
    #"Malo": "#dc3545",
#}

from pathlib import Path
import sys

def obtener_base_dir():
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[2]

BASE_DIR = obtener_base_dir()
DATABASE_PATH = BASE_DIR / "data" / "database" / "cacao.db"
IMAGES_DIR = BASE_DIR / "data" / "images"
APP_TITLE = "Clasificador de Calidad de Cacao con IA"

RESULTADOS_COLORES = {
    "Bueno": "#198754",
    "Regular": "#ffc107",
    "Malo": "#dc3545",
}
