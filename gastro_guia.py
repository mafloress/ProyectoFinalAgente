# gastro_guia.py
"""
Este script implementa el agente GastroGuía, un asistente culinario personal.
GastroGuía ayuda a los usuarios a encontrar recomendaciones de restaurantes
basándose en su ubicación y preferencias de comida.
"""

# Lista de restaurantes disponibles.
# Cada restaurante es un diccionario con su nombre, ubicación, tipo de cocina,
# una descripción para la recomendación y su platillo estrella.
RESTAURANTES = [
    {
        "nombre": "El Rincón del Taco Chilango",
        "ubicacion": "Ciudad de México, Condesa",
        "tipo_cocina": ["tacos", "mexicana", "tradicional"],
        "descripcion_recomendacion": "Auténticos tacos chilangos con el sazón de la abuela, ideales para una comida rápida y deliciosa.",
        "platillo_recomendado": "Tacos al pastor con todo"
    },
    {
        "nombre": "Mariscos Frescos 'El Faro'",
        "ubicacion": "Cancún, Zona Hotelera",
        "tipo_cocina": ["mariscos", "pescados", "frescos"],
        "descripcion_recomendacion": "Disfruta de los mariscos más frescos con vista al mar Caribe. Perfecto para una tarde calurosa.",
        "platillo_recomendado": "Ceviche mixto"
    },
    {
        "nombre": "Pizza Nostra",
        "ubicacion": "Guadalajara, Chapultepec",
        "tipo_cocina": ["italiana", "pizza", "pasta"],
        "descripcion_recomendacion": "Las mejores pizzas a la leña con ingredientes importados de Italia. ¡Como en casa de la nonna!",
        "platillo_recomendado": "Pizza Margherita con mozzarella di bufala"
    },
    {
        "nombre": "Verde Esmeralda Vegano",
        "ubicacion": "Monterrey, Barrio Antiguo",
        "tipo_cocina": ["vegana", "saludable", "orgánica"],
        "descripcion_recomendacion": "Cocina vegana creativa y deliciosa que te sorprenderá. ¡Prueba que comer sano no es aburrido!",
        "platillo_recomendado": "Hamburguesa de portobello con camote frito"
    },
    {
        "nombre": "Sakura Sushi & Roll",
        "ubicacion": "Ciudad de México, Polanco",
        "tipo_cocina": ["asiática", "sushi", "japonesa"],
        "descripcion_recomendacion": "Un rincón de Japón en Polanco. Sushi fresco y rollos innovadores en un ambiente elegante.",
        "platillo_recomendado": "Rollo Dragón Especial"
    },
    {
        "nombre": "Burger Joint MX",
        "ubicacion": "Tijuana, Zona Río",
        "tipo_cocina": ["hamburguesas", "americana", "malteadas"],
        "descripcion_recomendacion": "Hamburguesas gourmet con carne de primera y papas fritas caseras. ¡Para los verdaderos amantes de las burgers!",
        "platillo_recomendado": "Hamburguesa BBQ con tocino y aros de cebolla"
    },
    {
        "nombre": "Antojitos Doña Lupe",
        "ubicacion": "Puebla, Centro Histórico",
        "tipo_cocina": ["mexicana", "antojitos", "poblana"],
        "descripcion_recomendacion": "El auténtico sabor de la cocina poblana en cada platillo. ¡No te puedes perder las chalupas!",
        "platillo_recomendado": "Mole Poblano con arroz"
    },
    {
        "nombre": "El Asador Norteño",
        "ubicacion": "Hermosillo, Kino Bay",
        "tipo_cocina": ["carnes", "parrilla", "norteña"],
        "descripcion_recomendacion": "Cortes de carne calidad Sonora preparados a la parrilla. ¡El paraíso para los carnívoros!",
        "platillo_recomendado": "Rib eye añejo"
    },
    {
        "nombre": "Café de la Mañana",
        "ubicacion": "Oaxaca, Centro",
        "tipo_cocina": ["cafetería", "desayunos", "pan artesanal"],
        "descripcion_recomendacion": "Empieza tu día con un café oaxaqueño de altura y pan recién horneado. ¡El mejor lugar para desayunar!",
        "platillo_recomendado": "Chilaquiles rojos con tasajo y huevo"
    },
    {
        "nombre": "La Cochinita Feliz",
        "ubicacion": "Mérida, Paseo de Montejo",
        "tipo_cocina": ["yucateca", "cochinita pibil", "tradicional"],
        "descripcion_recomendacion": "La mejor cochinita pibil de Mérida, receta secreta de la familia. ¡Para chuparse los dedos!",
        "platillo_recomendado": "Torta de cochinita pibil"
    },
    {
        "nombre": "Curry & Canela",
        "ubicacion": "Ciudad de México, Roma Norte",
        "tipo_cocina": ["india", "curry", "especiada"],
        "descripcion_recomendacion": "Un viaje culinario a la India sin salir de la ciudad. Sabores exóticos y auténticos.",
        "platillo_recomendado": "Pollo Tikka Masala con arroz basmati"
    },
    {
        "nombre": "Tlayudas El Compadre",
        "ubicacion": "Oaxaca, Mercado Benito Juárez",
        "tipo_cocina": ["oaxaqueña", "tlayudas", "tradicional"],
        "descripcion_recomendacion": "Tlayudas gigantes y deliciosas, preparadas al momento con ingredientes frescos del mercado.",
        "platillo_recomendado": "Tlayuda con asiento, quesillo y chorizo"
    },
    {
        "nombre": "El Rincón Libanés",
        "ubicacion": "Ciudad de México, Del Valle",
        "tipo_cocina": ["libanesa", "árabe", "shawarma"],
        "descripcion_recomendacion": "Auténtica comida libanesa casera. Prueba nuestros kibbehs y hojas de parra.",
        "platillo_recomendado": "Shawarma de cordero"
    },
    {
        "nombre": "Pasta Fresca Ristorante",
        "ubicacion": "Querétaro, Juriquilla",
        "tipo_cocina": ["italiana", "pasta fresca", "artesanal"],
        "descripcion_recomendacion": "Pastas frescas hechas a mano todos los días con las recetas tradicionales de la nonna.",
        "platillo_recomendado": "Lasaña boloñesa clásica"
    },
    {
        "nombre": "Pozolería 'El Guerrero'",
        "ubicacion": "Guadalajara, Tlaquepaque",
        "tipo_cocina": ["mexicana", "pozole", "tradicional"],
        "descripcion_recomendacion": "El mejor pozole de Jalisco, estilo Guerrero. Rojo, blanco o verde, ¡todos deliciosos!",
        "platillo_recomendado": "Pozole rojo con carne de cerdo y tostadas"
    },
    {
        "nombre": "Arepas Venezolanas 'Mi Tierra'",
        "ubicacion": "Ciudad de México, Narvarte",
        "tipo_cocina": ["venezolana", "arepas", "empanadas"],
        "descripcion_recomendacion": "Prueba el auténtico sabor de Venezuela con nuestras arepas y empanadas. ¡Te sentirás como en casa!",
        "platillo_recomendado": "Arepa Reina Pepiada"
    }
]

# Función para dar la bienvenida al usuario y solicitar sus preferencias de comida y ubicación.
def solicitar_datos_usuario():
    """
    Imprime un mensaje de bienvenida y solicita al usuario su ubicación y el tipo de comida que desea.
    Todo esto en un ambiente amigable y en español mexicano.

    Returns:
        tuple: Una tupla que contiene dos cadenas de texto:
               - ubicacion_usuario (str): La ubicación ingresada por el usuario.
               - preferencia_comida_usuario (str): La preferencia de comida o antojo ingresado por el usuario.
    """
    print("¡Hola! Soy GastroGuía, tu asistente culinario personal. ¡Vamos a encontrar los mejores lugares para comer!")
    
    ubicacion_usuario = input("Por favor, dime dónde te encuentras o dónde quieres buscar (ej. 'Ciudad de México', 'Colonia Roma', 'cerca de mi trabajo'): ")
    preferencia_comida_usuario = input("¿Qué se te antoja comer hoy? (ej. 'tacos al pastor', 'sushi', 'algo picante y barato'): ")
    
    return ubicacion_usuario, preferencia_comida_usuario

# Función para recomendar restaurantes basándose en la ubicación y preferencia del usuario.
def recomendar_restaurantes(ubicacion_usuario, preferencia_usuario, lista_restaurantes):
    """
    Filtra la lista de restaurantes para encontrar aquellos que mejor coincidan
    con la ubicación y las preferencias culinarias del usuario.

    Args:
        ubicacion_usuario (str): La ubicación proporcionada por el usuario (ej. "Polanco", "cerca del Zócalo").
        preferencia_usuario (str): El tipo de comida o palabras clave del antojo del usuario (ej. "mariscos frescos", "tacos baratos").
        lista_restaurantes (list): La lista completa de diccionarios de restaurantes disponibles para buscar.

    Returns:
        list: Una lista que contiene hasta 3 diccionarios de restaurantes que cumplen con los criterios.
              Devuelve una lista vacía si no se encuentran coincidencias.
    """
    restaurantes_coincidentes = []
    ubicacion_usuario_lower = ubicacion_usuario.lower()
    preferencias_usuario_lower_split = preferencia_usuario.lower().split() # Dividir para buscar palabras clave

    for restaurante in lista_restaurantes:
        # Comprobación de ubicación: busca si la ubicación del usuario está contenida en la ubicación del restaurante.
        # Esto permite búsquedas más flexibles (ej. "Condesa" en "Ciudad de México, Condesa").
        coincidencia_ubicacion = ubicacion_usuario_lower in restaurante["ubicacion"].lower()

        # Comprobación de preferencia: busca si alguna palabra clave de la preferencia del usuario
        # coincide con alguna de las etiquetas de tipo de cocina del restaurante.
        coincidencia_preferencia = False
        if coincidencia_ubicacion: # Optimización: solo verificar preferencia si la ubicación ya coincidió.
            for palabra_preferencia in preferencias_usuario_lower_split:
                for tipo_cocina_restaurante in restaurante["tipo_cocina"]:
                    if palabra_preferencia in tipo_cocina_restaurante.lower():
                        coincidencia_preferencia = True
                        break # Salir del bucle de tipos de cocina si se encuentra una coincidencia.
                if coincidencia_preferencia:
                    break # Salir del bucle de palabras de preferencia si se encuentra una coincidencia.
        
        # Si ambas condiciones (ubicación y preferencia) se cumplen, se añade el restaurante.
        if coincidencia_ubicacion and coincidencia_preferencia:
            restaurantes_coincidentes.append(restaurante)

    # Devolver hasta un máximo de 3 restaurantes que coincidan.
    return restaurantes_coincidentes[:3]

# Función para mostrar las recomendaciones de restaurantes al usuario de forma clara y formateada.
def mostrar_recomendaciones(restaurantes_recomendados):
    """
    Presenta al usuario los restaurantes recomendados de una manera amigable y fácil de leer.
    Si no hay recomendaciones, informa al usuario.

    Args:
        restaurantes_recomendados (list): Una lista de diccionarios de restaurantes.
                                          Esta lista es generalmente el resultado de `recomendar_restaurantes`.
    """
    if not restaurantes_recomendados:
        print("\nLo siento, no encontré restaurantes que coincidan con tu búsqueda. ¡Quizás podríamos intentar con otros términos o una zona diferente!")
    else:
        print("\n¡Claro! Aquí tienes algunas recomendaciones especialmente para ti:")
        print("=" * 50) # Línea separadora para el encabezado.
        for i, restaurante in enumerate(restaurantes_recomendados):
            print(f"\nOpción #{i+1}:")
            print(f"  Nombre: {restaurante['nombre']}")
            print(f"  Ubicación: {restaurante['ubicacion']}")
            print(f"  Te lo recomiendo porque: {restaurante['descripcion_recomendacion']}")
            print(f"  No te pierdas: {restaurante['platillo_recomendado']}")
            if i < len(restaurantes_recomendados) - 1: # Añadir separador entre opciones, excepto para la última.
                print("-" * 30) 
        print("=" * 50) # Línea separadora para el final.
        print("¡Buen provecho!")
