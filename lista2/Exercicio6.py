def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "As matrizes fornecidas têm tamanhos diferentes e não podem ser somadas."
    resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    
    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matriz1, matriz2)

if isinstance(resultado, str):
    print(resultado)
else:
    print("Matriz resultante da soma:")
    for linha in resultado:
        print(linha)
