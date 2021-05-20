# LIBRERIA PANDAS
# Importar la libreria y se genera un alias 
import pandas as pd

# Crear Data frame estatico 
notasParcial=pd.DataFrame({'Estudiante':['Carolina','Andres','Camilo'],
                           'Nota Parcial':[3.8,4.7,5.0],
                           'Edad':[17,20,16]})

# Imprimir el Data frame
print(notasParcial)