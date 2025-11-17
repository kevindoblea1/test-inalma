
def is_palindrome(s: str) -> bool:
    """Devuelve True si s es palíndromo (ignorando espacios y mayúsculas)."""

    strLimpio = s.replace(' ', '').lower()
    strRevertido = strLimpio[::-1]

    return strLimpio == strRevertido

def compress_ranges(nums: list[int]) -> list[str]:
    """Comprime secuencias consecutivas:
    [1,2,3,5,7,8] -> ["1-3","5","7-8"]
    """
    rangos = []

    if not nums:
        return rangos
        
    inicio = nums[0]

    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
            fin = nums[i]

            if inicio == fin:
                rangos.append(str(inicio))
            else:
                rangos.append(f"{inicio}-{fin}")

            if i < len(nums) - 1:
                inicio = nums[i+1]

    return rangos

def min_path_sum(grid: list[list[int]]) -> int:
    """Suma mínima de camino desde (0,0) a (n-1,m-1) moviéndose solo derecha/abajo."""
    totalFilas = len(grid)
    totalColumnas = len(grid[0])

    sumaMinimaHasta = [[0 for _ in range(totalColumnas)] for _ in range(totalFilas)]
    sumaMinimaHasta[0][0] = grid[0][0]

    for columna in range(1, totalColumnas):
        sumaMinimaHasta[0][columna] = sumaMinimaHasta[0][columna - 1] + grid[0][columna]

    for fila in range(1, totalFilas):
        sumaMinimaHasta[fila][0] = sumaMinimaHasta[fila - 1][0] + grid[fila][0]

    for fila in range(1, totalFilas):
        for columna in range(1, totalColumnas):
            sumaDesdeArriba = sumaMinimaHasta[fila - 1][columna]
            sumaDesdeIzquierda = sumaMinimaHasta[fila][columna - 1]
            sumaMinimaActual = min(sumaDesdeArriba, sumaDesdeIzquierda)

            sumaMinimaHasta[fila][columna] = sumaMinimaActual + grid[fila][columna]

    return sumaMinimaHasta[totalFilas - 1][totalColumnas - 1]



def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    """Top k palabras por frecuencia; empate por orden alfabético ascendente."""

    if not words:
        return []

    frecuencias = {}

    for palabra in words:
        if palabra not in frecuencias:
            frecuencias[palabra] = 0
        frecuencias[palabra] += 1

    listaPalabras = list(frecuencias.items())
    listaPalabras.sort(key=lambda par: (-par[1], par[0]))

    resultado = [palabra for palabra, cantidad in listaPalabras[:k]]

    return resultado
