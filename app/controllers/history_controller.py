from app.services.database_service import DatabaseService

class HistoryController:
    def __init__(self):
        self.database_service = DatabaseService()

    def obtener_historial(self):
        return self.database_service.obtener_historial()

    def obtener_resumen(self):
        return self.database_service.obtener_resumen_resultados()
