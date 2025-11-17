# README Personal
## Autor
Sua Abigail Rubio Euceda

## Decisiones técnicas
### Lógica de programación (Python)
Implementé 4 funciones en "backend/src/algos/functions.py":

#### 1. is_palindrome(s: str) -> bool
- **Objetivo**: Verificar si una cadena es palíndromo ignorando espacios y mayúsculas
- **Enfoque**: 
  - Limpiar string: eliminar espacios y convertir a minúsculas
  - Revertir con slicing "[::-1]"
  - Comparar original limpio vs revertido

#### 2. compress_ranges(nums: list[int]) -> list[str]
- **Objetivo**: Comprimir números consecutivos en rangos
- **Enfoque**:
  - Iterar manualmente identificando inicio y fin de cada secuencia
  - Detectar ruptura cuando "nums[i+1] != nums[i] + 1"
  - Formatear como string individual o rango según corresponda

#### 3. min_path_sum(grid: list[list[int]]) -> int
- **Objetivo**: Encontrar suma mínima de camino de esquina superior izquierda a inferior derecha (solo movimientos derecha/abajo)
- **Enfoque**: Programación dinámica
  - Crear matriz "sumaMinimaHasta[fila][columna]" que guarda la suma mínima hasta cada celda
  - Primera fila: solo suma acumulada
  - Primera columna: solo suma acumulada
  - Resto: "min(desde_arriba, desde_izquierda) + valor_actual"

#### 4. top_k_frequent_words(words: list[str], k: int) -> list[str]
- **Objetivo**: Top k palabras más frecuentes, empates se resuelven alfabéticamente
- **Enfoque**:
  - Contar frecuencias con diccionario manual
  - Convertir a lista de tuplas "(palabra, frecuencia)"
  - Ordenar con criterio compuesto: "-frecuencia" descendente, luego "palabra" ascendente
  - Tomar primeros k elementos

### Backend
- Solo fue necesario ajustar dos archivos para pasar los tests:
  - **models.py**: Agregué "ordering = ["id"]" para evitar el warning de paginación con objetos sin orden
  - **serializers.py**: Configuré "extra_kwargs" con "coerce_to_string: False" para que "price" se retorne como número en lugar de string, permitiendo el ordenamiento correcto en el test

### Frontend
- Refactoricé la ubicación del debounce:
  - **Antes**: El debounce estaba dentro de "SearchBar", usando "useDebounce" internamente
  - **Después**: Moví el debounce a "App.jsx", donde se consume el API
  - **Razón**: Centralizar la lógica de búsqueda y simplificar "SearchBar" (principio de responsabilidad única)

## Problemas encontrados y soluciones
### Backend
- **Problema**: Test "test_tags_and_ordering" fallaba porque el ordenamiento no funcionaba correctamente
- **Causa**: El serializer retornaba "price" como string ("299.99"), y el test ordenaba alfabéticamente
- **Solución**: Configurar "coerce_to_string: False" para que "price" sea número

### Frontend
- **Problema**: Test esperaba exactamente 2 llamadas al API con debounce de 300ms
- **Causa**: El debounce estaba duplicado (en SearchBar y en App)
- **Solución**: Remover debounce de SearchBar y manejarlo solo en App