from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QScrollArea, QFrame
)

class TumacoInfoView(QWidget):
    def __init__(self):
        super().__init__()
        self._crear_interfaz()

    def _crear_interfaz(self):
        layout_principal = QVBoxLayout(self)

        titulo = QLabel("Lo que necesitas saber sobre el cacao de Tumaco")
        titulo.setObjectName("tituloPrincipal")
        titulo.setAlignment(Qt.AlignCenter)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        contenedor = QWidget()
        layout_contenido = QVBoxLayout(contenedor)
        layout_contenido.setSpacing(15)

        seccion_1 = self.crear_seccion(
            "1. Importancia del cacao en Tumaco",
            "El cacao producido en Tumaco, Nariño, es reconocido a nivel nacional e internacional por su alta calidad, características organolépticas y potencial como cacao fino de aroma. Esta actividad representa una de las principales fuentes de ingreso para muchas familias rurales de la región, contribuyendo al desarrollo económico y social del territorio. \n"
            "Además, el cultivo de cacao ha sido promovido como una alternativa sostenible frente a economías ilícitas, fortaleciendo procesos de sustitución de cultivos y fomentando prácticas agrícolas responsables. En este sentido, el cacao no solo tiene valor comercial, sino también un impacto significativo en la construcción de tejido social y desarrollo regional."
            "puede aportar al desarrollo rural, la generación de empleo y el mejoramiento de la calidad de vida."
        )

        seccion_2 = self.crear_seccion(
            "2. Condiciones del territorio",
            "El municipio de Tumaco presenta condiciones agroecológicas favorables para el cultivo de cacao. Entre sus principales características se destacan: \n" 
            "Clima tropical húmedo, con temperaturas promedio entre 25°C y 28°C. Alta pluviosidad, lo que favorece el crecimiento del cultivo. Suelos ricos en materia orgánica, adecuados para el desarrollo del cacao. Ubicación geográfica estratégica, cercana a la costa pacífica. \n"
            ""
            "Sin embargo, estas mismas condiciones también pueden generar desafíos, como el exceso de humedad, que favorece la aparición de enfermedades en el cultivo."
        )

        seccion_3 = self.crear_seccion(
            "3. Factores que influyen en la calidad",
            "La calidad del cacao depende de múltiples factores a lo largo de su proceso productivo, entre los cuales se destacan: \n "
            "Genética del cultivo: tipo de cacao (criollo, forastero o trinitario). \n"
            "Manejo agronómico: prácticas de siembra, poda y control de plagas. \n" 
            "Proceso de fermentación: fundamental para el desarrollo de aroma y sabor. \n" 
            "Secado del grano: influye en la conservación y calidad final. \n" 
            "Condiciones ambientales: humedad, temperatura y exposición solar. \n" 
            "Manipulación postcosecha: almacenamiento y transporte. \n"
            "Una mala gestión en cualquiera de estos factores puede afectar negativamente la calidad del producto final."
        )

        seccion_4 = self.crear_seccion(
            "4. Problemas frecuentes en el cacao",
            "En la producción de cacao en Tumaco se presentan diversas problemáticas que afectan la calidad y productividad, entre ellas: \n "
            "Enfermedades como la moniliasis y la escoba de bruja. \n"
            "Exceso de humedad, que puede generar moho en los granos. \n"  
            "Fermentación inadecuada, que afecta el sabor y aroma. \n" 
            "Secado deficiente, generando granos de baja calidad. \n"
            "Falta de estandarización en la clasificación, lo que genera inconsistencias. \n"
            "Limitado por falta de acceso a tecnología, dificultando la modernización del proceso. \n"
            "Estas problemáticas justifican la necesidad de implementar soluciones tecnológicas que apoyen al productor. "
        )

        seccion_5 = self.crear_seccion(
            "5. Utilidad de la inteligencia artificial en este proyecto",
            "La inteligencia artificial, específicamente la visión artificial, permite analizar imágenes digitales del cacao para identificar patrones relacionados con su calidad, como color, textura y posibles defectos. \n"
            "En este proyecto, la IA se utiliza para: \n "
            "Automatizar el proceso de clasificación del cacao. \n"
            "Reducir la subjetividad en la evaluación manual. \n"
            "Generar resultados rápidos y consistentes. \n"
            "Apoyar la toma de decisiones basadas en datos. \n"
            "De esta manera, la inteligencia artificial se convierte en una herramienta innovadora que contribuye a mejorar la eficiencia y precisión en la evaluación del producto. \n"
        )

        seccion_6 = self.crear_seccion(
            "6. Beneficios para productores y evaluadores",
            "La implementación de este sistema genera múltiples beneficios: \n"
            "Para productores: \n"
            "Mejora en la calidad del producto.\n"
            "Mayor valor comercial del cacao.\n"
            "Reducción de pérdidas por mala clasificación.\n"
            "Acceso a tecnología innovadora.\n"
            "pero sí lo complementa con apoyo tecnológico.\n"
            "Para evaluadores: \n"
            "Apoyo en la toma de decisiones.\n"
            "Reducción de errores humanos.\n"
            "Mayor rapidez en la clasificación.\n"
            "Estandarización del proceso de evaluación.\n"
            "\n"
            "En conjunto, estos beneficios contribuyen al fortalecimiento del sector cacaotero y a la competitividad de la región."

        )

        layout_contenido.addWidget(seccion_1)
        layout_contenido.addWidget(seccion_2)
        layout_contenido.addWidget(seccion_3)
        layout_contenido.addWidget(seccion_4)
        layout_contenido.addWidget(seccion_5)
        layout_contenido.addWidget(seccion_6)
        layout_contenido.addStretch()

        scroll.setWidget(contenedor)

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(scroll)

    def crear_seccion(self, titulo, contenido):
        marco = QFrame()
        marco.setObjectName("seccionInfo")

        layout = QVBoxLayout(marco)

        label_titulo = QLabel(titulo)
        label_titulo.setObjectName("subtituloInfo")

        texto = QTextEdit()
        texto.setReadOnly(True)
        texto.setPlainText(contenido)
        texto.setObjectName("textoInfo")
        texto.setMinimumHeight(110)

        layout.addWidget(label_titulo)
        layout.addWidget(texto)

        return marco