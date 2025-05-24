# GastroGuía: Tu Asistente Culinario Personal
Miguel Ángel Flores Saldívar

## Uso de LLMs y Agentes IA
Se utilizaron los siguientes LLMs para poder tomar ideas para tomar la base del proyecto y buscar fuentes reales de datos para el proyecto, se hizo la comparativa entre cada respuesta de cada uno y se escogío la mas ad hoc:
- Gemini
- Copilot
- Deepseek
- ChatGPT

Se utilizó adicional para documentación e implementación en Github:
- Jules Google
  
## Descripción Breve

GastroGuía es un agente inteligente diseñado para ayudarte a descubrir tu próxima comida deliciosa. Su propósito principal es recomendarte restaurantes basándose en tu ubicación actual o deseada y tus preferencias culinarias o antojos del momento. ¡Dile a GastroGuía dónde estás y qué se te antoja, y te dará algunas sugerencias! Se hicieron dos propuestas una en python con datos prescritos y otro desarrollado en Google AI Studio (archivo: gastroguía.zip)

## Cómo Funciona (Descripción General)

El funcionamiento de GastroGuía es sencillo:

*   **Base de Datos Interna:** En esta versión, GastroGuía utiliza una base de datos interna y ficticia de restaurantes. Esta lista contiene información variada sobre diferentes establecimientos.
*   **Interacción con el Usuario:** Al iniciar, el agente te hará dos preguntas clave:
    1.  Tu ubicación (o dónde te gustaría buscar restaurantes).
    2.  Una descripción de lo que te apetece comer (tu antojo o preferencia).
*   **Búsqueda y Recomendación:** Con esta información, GastroGuía buscará en su base de datos los restaurantes que mejor se adapten a tus criterios y te presentará hasta tres opciones recomendadas.

## Cómo Ejecutar el Agente

Para poner en marcha a GastroGuía y recibir tus recomendaciones, sigue estos pasos:

1.  **Requisito:** Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).
2.  **Ejecución:** Abre una terminal o línea de comandos, navega hasta el directorio donde guardaste el archivo `gastro_guia.py` y ejecuta el siguiente comando:
    ```bash
    python gastro_guia.py
    ```
3.  **Interacción:** Una vez ejecutado, GastroGuía te saludará y comenzará a hacerte preguntas directamente en la consola para obtener tu ubicación y preferencias.

## Entrada Esperada

Para que GastroGuía pueda hacer su magia, necesitará que le proporciones la siguiente información:

*   **Ubicación:**
    *   Puedes ser tan general o específico como desees. Por ejemplo:
        *   "Ciudad de México"
        *   "Colonia Roma"
        *   "Cerca del Ángel de la Independencia"
        *   "Guadalajara, Chapultepec"
    *   El agente intentará encontrar coincidencias basadas en la información que le des.

*   **Preferencia de Comida:**
    *   Describe qué tipo de comida se te antoja. ¡Sé creativo! Por ejemplo:
        *   "Tacos al pastor"
        *   "Sushi fresco"
        *   "Algo picante y barato"
        *   "Comida italiana tradicional"
        *   "Un buen corte de carne"
        *   "Opciones veganas"

## Salida del Agente

Si GastroGuía encuentra restaurantes que coincidan con tu búsqueda, te presentará hasta tres recomendaciones con el siguiente formato:

*   **Nombre del Restaurante:** El nombre del establecimiento.
*   **Ubicación:** Dónde se encuentra el restaurante.
*   **Recomendación:** Una breve descripción de por qué se te recomienda ese lugar.
*   **Platillo Estrella:** El platillo más destacado o recomendado del lugar.

Si no encuentra coincidencias, te informará amablemente para que puedas intentar con diferentes criterios.

## Notas Adicionales

*   **Versión Inicial:** Esta es una versión temprana de GastroGuía. La base de datos de restaurantes es ficticia, limitada y creada con fines demostrativos.
*   **Futuras Mejoras:** ¡Hay muchas ideas para hacer GastroGuía aún mejor! Algunas posibilidades incluyen:
    *   Conectar el agente a una API real de restaurantes (ej. Google Places, Yelp) para obtener datos actualizados y más amplios.
    *   Expandir significativamente la base de datos interna con más variedad y detalles.
    *   Mejorar la lógica de búsqueda y emparejamiento para entender consultas más complejas o ambiguas.
    *   Añadir filtros por precio, calificación, o servicios específicos.
    *   Desarrollar una interfaz gráfica de usuario (GUI) o una integración con chatbots.

¡Esperamos que disfrutes usando GastroGuía!
