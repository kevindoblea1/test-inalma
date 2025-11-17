# AI_USAGE 

## Herramientas usadas 
- Stack Overflow (consultas puntuales sobre sintaxis)
- El Libro de Python (ellibrodepython.com)
- FreeCodeCamp 
- Programiz
- Documentación oficial de Django/DRF
- YouTube (tutoriales sobre matrices y estructuras de datos en Python)

## Prompts o consultas clave (resumen) 
- "trim python" 
- "reverse string python" 
- "listas python"
- "matrices python"
- "diccionario python"
- "expresiones lambda python"
- "pytest python"
- "lambda python"
- "que es django"
- "django serializers"
- "debounce react"


## Qué encontré y cómo lo adapté 
### is_palindrome()
- **Busqué:** Cómo eliminar espacios y cómo invertir strings en Python
- **Encontré:** Métodos ".replace(' ', '')" y slicing "[::-1]" en Stack Overflow
- **Cómo lo usé:** Combiné ambas técnicas para crear mi propia implementación comparando la cadena limpia con su versión invertida
- **Adaptación propia:** Implementé la lógica completa de validación yo misma

### compress_ranges()
- **Busqué:** Documentación sobre listas en Python
- **Fuente:** El Libro de Python
- **Qué aprendí:** Manejo de listas, append, indices, iteración
- **Cómo lo usé:** Desarrollé la lógica desde cero usando listas para detectar rangos consecutivos

### min_path_sum()
- **Busqué:** "matrices python", "2D arrays python"
- **Fuentes:** Programiz, tutoriales de YouTube
- **Qué aprendí:** Cómo acceder a elementos con "[fila][columna]", iterar matrices, diferencias con C#
- **Adaptación propia:** Traduje la lógica que conocía de C# a Python, ajustando la sintaxis y forma de recorrer matrices
- **Desafío:** Al inicio se me dificultó, revisé varios videos y ejemplos hasta entender bien el concepto

### top_k_frequent_words()
- **Busqué:** "diccionarios python", "expresiones lambda python"
- **Fuentes:** El Libro de Python, FreeCodeCamp
- **Qué aprendí:** Cómo usar diccionarios para contar, ordenamiento con lambda
- **Adaptación propia:** Implementé la lógica de conteo y usé sorted() con lambda para ordenar por frecuencia y alfabéticamente
- **Comparación:** Me apoyé en mi conocimiento de C# para entender la equivalencia de estructuras

### Entendimiento de tests
- **Busqué:** "pytest python", "cómo funcionan los tests en python"
- **Fuente:** El Libro de Python (ellibrodepython.com)
- **Qué aprendí:**
  - Pytest detecta funciones que empiezan con "test_"
  - "assert" valida que el resultado sea el esperado
  - Cómo interpretar output de pytest (PASSED/FAILED)
- **Cómo lo usé:** Para entender qué validaban los tests y verificar que mis soluciones fueran correctas

### Backend
- **Busqué:** "models django", "coerce_to_string django rest framework"
- **Fuentes:** Documentación oficial de DRF, Stack Overflow
- **Qué aprendí:** 
  - Django requiere "ordering" en Meta para paginación consistente
  - DRF por defecto convierte DecimalField a string por precisión
- **Adaptación propia:** 
  - Agregué "ordering = ["id"]" en models.py
  - Configuré "coerce_to_string: False" en serializers.py

### Frontend
- **Busqué:** "hooks react", "debounce react"
- **Fuentes:** Documentación oficial de React, tutoriales
- **Qué aprendí:** 
  - Que son los hooks en react
  - Dónde ubicar la lógica de debounce
- **Adaptación propia:** 
  - Moví debounce de SearchBar a App por principio de responsabilidad única
  - Implementé cleanup para evitar actualizaciones después de desmontar

## Fuentes citadas 
- https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-string
- https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
- https://ellibrodepython.com/listas-en-python
- https://ellibrodepython.com/diccionarios-en-python
- https://ellibrodepython.com/python-testing
- https://www.programiz.com/python-programming/matrix
- https://www.freecodecamp.org/espanol/news/expresiones-lambda-en-python/
- https://www.django-rest-framework.org/
- https://www.django-rest-framework.org/api-guide/serializers/
- https://docs.djangoproject.com/en/5.2/topics/db/models/
- https://docs.djangoproject.com/en/5.2/topics/serialization/
- https://www.freecodecamp.org/espanol/news/debouncing-en-react-como-retrasar-una-funcion-en-js/

## Notas de ética/seguridad 
- No subí secretos ni credenciales a ninguna plataforma
- No copié código propietario
- Solo consulté recursos públicos, documentación oficial y comunidades abiertas
- Las búsquedas fueron específicas sobre sintaxis y conceptos, no solicitudes de código completo