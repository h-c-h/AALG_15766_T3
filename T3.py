lab = [[1, 1, 1, 3, 0, 1, 1, 1, 4],
       [3, 0, 0, 1, 0, 1, 0, 0, 1],
       [1, 1, 0, 1, 1, 1, 0, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 1, 0],
       [1, 1, 1, 1, 1, 1, 3, 1, 1],
       [3, 0, 1, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 3, 1, 1, 1, 0, 4],
       [1, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 1, 3, 1, 0, 1, 1, 1, 1]]

res = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},", end="")
        print()
    print()

def valida(fil, col):
    if fil < 0 or fil >= 9:
        return False
    if col < 0 or col >= 9:
        return False
    if lab[fil][col] == 0:
        return False
    if res[fil][col] == 1:
        return False
    return True

def labPuntos(fil, col, puntos):
    if fil == 0 and col == 0:
        puntos += lab[fil][col]
        if puntos >= 23:
            res[fil][col] = 1
            imprime(res)
            print("Camino encontrado con al menos 23 puntos Total:", puntos)
            return True
        else:
            return False
    else:
        if valida(fil, col):
            puntos += lab[fil][col]
            res[fil][col] = 1
            if labPuntos(fil - 1, col, puntos):
                return True
            elif labPuntos(fil, col + 1, puntos):
                return True
            elif labPuntos(fil + 1, col, puntos):
                return True
            elif labPuntos(fil, col - 1, puntos):
                return True
            else:
                res[fil][col] = 0
                return False
        else:
            return False

print("laberinto incial:")
imprime(lab)

if labPuntos(8, 0, 0):
    print("Salida exitosa.")
else:
    print("No hay salida")
    imprime(res)
