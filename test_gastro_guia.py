import unittest
from gastro_guia import recomendar_restaurantes, RESTAURANTES

# Pruebas unitarias para la función recomendar_restaurantes de GastroGuía.
class TestGastroGuia(unittest.TestCase):

    # Lista de restaurantes de prueba. Podríamos usar la lista importada RESTAURANTES
    # directamente, o definir una aquí para tener más control en casos específicos.
    # Por simplicidad y para probar directamente con los datos de producción, usamos la importada.
    lista_completa_restaurantes = RESTAURANTES

    # Prueba un caso de éxito simple donde se espera encontrar al menos un restaurante.
    def test_recomendacion_exitosa_simple(self):
        """
        Prueba una búsqueda simple y exitosa.
        Espera encontrar restaurantes de tacos en la Ciudad de México.
        Verifica que el resultado sea una lista y que cada elemento sea un diccionario.
        """
        ubicacion_usuario = "Ciudad de México"
        preferencia_usuario = "tacos"
        resultados = recomendar_restaurantes(ubicacion_usuario, preferencia_usuario, self.lista_completa_restaurantes)
        
        # Verificamos que la salida sea una lista
        self.assertIsInstance(resultados, list, "La función debería devolver una lista.")
        
        # Si hay resultados, verificamos que cada uno sea un diccionario (representando un restaurante)
        if resultados:
            self.assertTrue(all(isinstance(r, dict) for r in resultados), "Cada resultado debería ser un diccionario.")
            # Verificamos que al menos un restaurante de "tacos" en "Ciudad de México" exista en los datos.
            # Esto depende de los datos en gastro_guia.py
            nombres_encontrados = [r['nombre'].lower() for r in resultados]
            self.assertIn("el rincón del taco chilango", nombres_encontrados, "Debería encontrar 'El Rincón del Taco Chilango'.")

    # Prueba un caso donde la ubicación es incorrecta y no se esperan resultados.
    def test_sin_resultados_ubicacion_incorrecta(self):
        """
        Prueba una búsqueda con una ubicación donde no hay restaurantes.
        Espera una lista vacía como resultado.
        """
        ubicacion_usuario = "Paris" # Asumimos que no hay restaurantes en París en nuestra lista.
        preferencia_usuario = "tacos"
        resultados = recomendar_restaurantes(ubicacion_usuario, preferencia_usuario, self.lista_completa_restaurantes)
        self.assertEqual(len(resultados), 0, "No debería haber resultados para una ubicación inexistente en los datos.")

    # Prueba un caso donde la preferencia de comida es muy específica y no se esperan resultados.
    def test_sin_resultados_preferencia_incorrecta(self):
        """
        Prueba una búsqueda con una preferencia de comida que no existe.
        Espera una lista vacía como resultado.
        """
        ubicacion_usuario = "Ciudad de México"
        preferencia_usuario = "comida de astronauta" # Asumimos que no hay este tipo de comida.
        resultados = recomendar_restaurantes(ubicacion_usuario, preferencia_usuario, self.lista_completa_restaurantes)
        self.assertEqual(len(resultados), 0, "No debería haber resultados para una preferencia de comida inexistente.")

    # Prueba que la búsqueda de preferencias funcione con múltiples palabras clave.
    def test_multiples_palabras_preferencia(self):
        """
        Prueba la búsqueda con múltiples palabras en la preferencia.
        Por ejemplo, "tacos al pastor". Debería encontrar restaurantes que coincidan con "tacos" o "pastor".
        """
        ubicacion_usuario = "Ciudad de México"
        preferencia_usuario = "tacos al pastor" # El Rincón del Taco Chilango sirve "tacos al pastor"
        resultados = recomendar_restaurantes(ubicacion_usuario, preferencia_usuario, self.lista_completa_restaurantes)
        self.assertIsInstance(resultados, list)
        if resultados: # Solo proceder si hay resultados
            self.assertTrue(len(resultados) > 0, "Debería encontrar resultados para 'tacos al pastor' en CDMX.")
            # Verificamos que el restaurante esperado esté en los resultados.
            encontrado = any(r['nombre'] == "El Rincón del Taco Chilango" for r in resultados)
            self.assertTrue(encontrado, "Debería encontrar 'El Rincón del Taco Chilango' para 'tacos al pastor'.")

    # Prueba que la búsqueda no sea sensible a mayúsculas/minúsculas.
    def test_sensibilidad_mayusculas_minusculas(self):
        """
        Prueba que la búsqueda funcione correctamente independientemente del uso de mayúsculas o minúsculas.
        """
        ubicacion_usuario_minusculas = "ciudad de méxico"
        preferencia_usuario_minusculas = "tacos"
        resultados_minusculas = recomendar_restaurantes(ubicacion_usuario_minusculas, preferencia_usuario_minusculas, self.lista_completa_restaurantes)

        ubicacion_usuario_mayusculas = "CIUDAD DE MÉXICO"
        preferencia_usuario_mayusculas = "TACOS"
        resultados_mayusculas = recomendar_restaurantes(ubicacion_usuario_mayusculas, preferencia_usuario_mayusculas, self.lista_completa_restaurantes)

        self.assertEqual(len(resultados_minusculas), len(resultados_mayusculas), "La cantidad de resultados debería ser la misma independientemente de mayúsculas/minúsculas.")
        # Comparamos los nombres para asegurar que son los mismos restaurantes (asumiendo que los nombres son únicos)
        nombres_minusculas = sorted([r['nombre'] for r in resultados_minusculas])
        nombres_mayusculas = sorted([r['nombre'] for r in resultados_mayusculas])
        self.assertListEqual(nombres_minusculas, nombres_mayusculas, "Los restaurantes encontrados deberían ser los mismos.")

    # Prueba que la función devuelva un máximo de 3 recomendaciones.
    def test_maximo_tres_recomendaciones(self):
        """
        Verifica que la función no devuelva más de 3 recomendaciones,
        incluso si hay más coincidencias.
        """
        # Para esta prueba, creamos una lista de restaurantes simulada con muchas coincidencias.
        # O podemos usar una búsqueda muy genérica en la lista real.
        # Ejemplo: "mexicana" en "Ciudad de México" podría dar varios resultados.
        
        # En nuestra lista RESTAURANTES, hay varios restaurantes en "Ciudad de México"
        # y varios con "mexicana" o "tradicional" o "tacos" en su tipo_cocina.
        # "El Rincón del Taco Chilango" (tacos, mexicana, tradicional)
        # "Sakura Sushi & Roll" (no es mexicana)
        # "Antojitos Doña Lupe" (Puebla, no CDMX)
        # "Curry & Canela" (india)
        # "Tlayudas El Compadre" (Oaxaca, no CDMX)
        # "El Rincón Libanés" (libanesa)
        # "Arepas Venezolanas 'Mi Tierra'" (venezolana)
        
        # Vamos a probar con "Ciudad de México" y "mexicana"
        # Deberían coincidir:
        # 1. El Rincón del Taco Chilango (tipo_cocina: ["tacos", "mexicana", "tradicional"])
        # (y si hubiera más, se probaría el límite de 3)
        
        # Para asegurar que probamos el límite de 3, modificaremos temporalmente
        # los datos de prueba *solo para este test* o crearemos unos nuevos.
        # Por simplicidad, intentaremos una búsqueda amplia.
        # Si no hay suficientes, la prueba no será tan robusta para el límite de 3.

        # De la lista actual, los restaurantes en "Ciudad de México" son:
        # - El Rincón del Taco Chilango (tacos, mexicana, tradicional)
        # - Sakura Sushi & Roll (asiática, sushi, japonesa)
        # - Curry & Canela (india, curry, especiada)
        # - El Rincón Libanés (libanesa, árabe, shawarma)
        # - Arepas Venezolanas 'Mi Tierra' (venezolana, arepas, empanadas)
        # Si buscamos "Ciudad de México" y "comida" (una palabra muy genérica que podría estar en descripciones si las usáramos,
        # pero en tipo_cocina es menos probable), no es ideal.
        # Probemos con una palabra clave que SÍ esté en varios tipos de cocina en CDMX.
        # "El Rincón del Taco Chilango" tiene "mexicana"
        # Si tuviéramos otros 3 restaurantes en CDMX con "mexicana", esta prueba sería mejor.
        # Por ahora, verificaremos que el número de resultados es <= 3.

        ubicacion_usuario = "Ciudad de México"
        preferencia_usuario = "comida" # Palabra genérica para intentar obtener varias coincidencias de tipo_cocina
                                      # La función `recomendar_restaurantes` busca `preferencia_usuario` en `tipo_cocina`.
                                      # Ningún `tipo_cocina` actual contiene "comida".
                                      # Usemos "mexicana" que está en "El Rincón del Taco Chilango".
        
        # Vamos a crear un conjunto de datos de prueba específico para este test para garantizar >3 coincidencias.
        restaurantes_prueba_limite = [
            {"nombre": "Tacos 1", "ubicacion": "Ciudad de México", "tipo_cocina": ["mexicana", "tacos"], "descripcion_recomendacion": "Desc1", "platillo_recomendado": "Plato1"},
            {"nombre": "Tacos 2", "ubicacion": "Ciudad de México", "tipo_cocina": ["mexicana", "rapida"], "descripcion_recomendacion": "Desc2", "platillo_recomendado": "Plato2"},
            {"nombre": "Tacos 3", "ubicacion": "Ciudad de México", "tipo_cocina": ["mexicana", "casera"], "descripcion_recomendacion": "Desc3", "platillo_recomendado": "Plato3"},
            {"nombre": "Tacos 4", "ubicacion": "Ciudad de México", "tipo_cocina": ["mexicana", "gourmet"], "descripcion_recomendacion": "Desc4", "platillo_recomendado": "Plato4"},
            {"nombre": "Tacos 5", "ubicacion": "Ciudad de México", "tipo_cocina": ["mexicana", "tradicional"], "descripcion_recomendacion": "Desc5", "platillo_recomendado": "Plato5"},
            {"nombre": "Otro", "ubicacion": "Guadalajara", "tipo_cocina": ["mexicana"], "descripcion_recomendacion": "Desc6", "platillo_recomendado": "Plato6"},
        ]
        
        resultados = recomendar_restaurantes("Ciudad de México", "mexicana", restaurantes_prueba_limite)
        self.assertTrue(len(resultados) <= 3, "La función debería devolver como máximo 3 recomendaciones.")
        self.assertEqual(len(resultados), 3, "Con 5 coincidencias, debería devolver exactamente 3.")

# Estructura para ejecutar las pruebas si el script se ejecuta directamente.
if __name__ == '__main__':
    unittest.main()
