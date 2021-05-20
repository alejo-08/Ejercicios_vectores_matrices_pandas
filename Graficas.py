# Importacion de librerias 
import matplotlib 
import matplotlib.pyplot as plt


# Generar datos 
# Interactuar con listas 
nombreProductos=['Arroz','Azucar','Vino','Leche']
ventaProductos=[100,50,30,20]


# Funciones que resuelven las preguntas 

def totalVentas():
    sumTotVen=0
    for pos in range(4):
        sumTotVen= sumTotVen+ventaProductos[pos]
    return sumTotVen
    
def promVenTot():
    promVen= 0.0
    promVen=totalVentas()/len(ventaProductos)
    return(promVen)
    
# Llamar a la funcion
print("El total de ventas es: ",totalVentas())
print("El promedio de ventas es: ",promVenTot())    


# Generar el gráfico
fig,ax= plt.subplots()
ax.set_title('VENTAS DE LA EMPRESA')
ax.set_ylabel('Valor')
ax.set_xlabel('Nombre Producto')

# Crear grafico 
plt.bar(nombreProductos,ventaProductos)
plt.show()


    
