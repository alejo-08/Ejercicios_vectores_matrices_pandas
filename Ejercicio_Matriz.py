# MATRICES 
# 1. Declarar la matriz
matrizNumeros=[[12,32,56,48],
               [8, 48, 18,58],
               [2, 4 , 6, 8]]


# 2. Imprimr la matriz 
print(matrizNumeros)

# 3. Imprimir una posicion fija
print("Posicion especifica:",matrizNumeros[0][2])

# 4. Solcitar la posicion del usuario 
fil=int(input("Fila: "))
col=int(input("Columna: "))
print("Posicion leida por teclado:",matrizNumeros[fil-1][col-1])

# 5. Imprimir una fila determinada 
print("Fila 0:",matrizNumeros[0])
print("Fila 1:",matrizNumeros[1])
print("Fila 2:",matrizNumeros[2])

# 6. Imprimir una columna
for f in range (3):
    print (matrizNumeros[f][1])
    
# 7. Imprimir la columna  que el usuario quiera
col=int(input("Columna que desea imprimir: "))
for f in range(3):
    print(matrizNumeros[f][col])

# 8. Sumar todos los elementos de la matriz 
sumElemat=0
for f in range(3):
    for c in range(4):
        sumElemat=sumElemat+matrizNumeros[f][c]
print("La suma de los elementos es: ",sumElemat)

# Sumar e imprimir los elementos de cada fila
print("Sumar e imprimir los elementos de cada fila")
sumElemat=0
for f in range(3):
    for c in range(4):
        sumElemat=sumElemat+matrizNumeros[f][c]
    print("La suma de los elementos es: ",sumElemat)
    sumElemat=0




