# Ordenamiento burbuja

#Definicion de un vector 

#listaEnteros=[30,15,20,45,2,5,6,8,9,10]

listaEnteros=[]
def cargarDatos(listaEnteros):
    for i in range (10):
        valor=int(input("Digite el valor:"))
        listaEnteros.append(valor)
    print("La lista desordenada es:",listaEnteros)
      
# Funcion que realiza el ordenamient burbuja

def ordBurbuja(listaDesordenada):
    for i in range (1,len(listaDesordenada)-1): 
        for j in range (0,len(listaDesordenada)-1):
            if listaDesordenada[j]>listaDesordenada[j+1]:
                aux=listaDesordenada[j]
                listaDesordenada[j]=listaDesordenada[j+1]
                listaDesordenada[j+1]=aux
    print("La lista ordenada es:",listaEnteros)         
# Fin del ordenamiento

# Llamar la funcion que carga los datos 
cargarDatos(listaEnteros)

# Llamar la funcion ordenar burbuja 
ordBurbuja(listaEnteros)
   
        
    