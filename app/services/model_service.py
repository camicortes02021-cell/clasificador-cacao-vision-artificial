class ModelService:
    def predecir(self, caracteristicas):
        promedio_color = caracteristicas["promedio_color"]
        textura = caracteristicas["nivel_textura"]

        if 85 <= promedio_color <= 165 and textura >= 35:
            return {
                "resultado": "Bueno",
                "confianza": 91.4,
                "observacion": "La muestra presenta apariencia uniforme y textura favorable."
            }

        if 60 <= promedio_color <= 190 and 20 <= textura < 35:
            return {
                "resultado": "Regular",
                "confianza": 78.2,
                "observacion": "La muestra tiene características intermedias y requiere revisión adicional."
            }

        return {
            "resultado": "Malo",
            "confianza": 88.6,
            "observacion": "La muestra presenta rasgos visuales poco favorables para calidad alta."
        }
