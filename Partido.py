#  Lectura de archivos tipo excel
#  Importar librerías
import pandas as pd

#  Leer archivo excel
df_partidos = pd.read_excel('Futbol_Partidos.xlsx')
print(df_partidos)
