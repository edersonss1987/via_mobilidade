#Analise de dados via mobilidade

#importe dos pacotes
import pandas as pd
import numpy as np
import os
from getpass import getpass
from time import time



#criando o dataframe apartir do arquivo
df = pd.read_csv('/content/via_mobilidade/traffic.csvv', sep=';')

# Verificando a quantidade de colunas e linhas 
df.shape

# Como podemos verificar, todas as linhas estão preenchidas, não possuindo valores nulos, isso é muito bom para os proximos passos.
#verificamos também os tipos de dados, que aparentemente estão em um formato correto
df.info()

#Realizando a leitura das primeiras 5 linhas do arquivo
df.head()


### **1.1. Nativo** 
#> O que o código abaixo computa?
#**Resposta**: O Código abaixo calcula todos os incidentes que aconteceram nos interlos de horários entre 7h00 e 20h00 dos dias 14, 15, 16, 17 e 18.

 #No inicio do código, o arquivo é lido, linha após linha, com separação de caracteres e quebra de linha armazenados em uma variavél.
 #Em seguida os elementos são somados um a um, desde o segundo elemento ao 16, sendo assim o indices 0 e 17 são eliminados do calculo.

 #Por fim, é impresso os valores reprentando os intevalos de dias.


# -- read
inicio = time ()

data = None

with open(file='traffic.csv', mode='r', encoding='utf8') as fp:
  
  fp.readline()
  data = fp.read()

# -- analytics

day = 14
incidents = 0
incident_by_day = dict()
# print(f'{incident_by_day}, {incidents},{incident_by_day}')

for timebox in data.split(sep='\n'):
  timebox_data = timebox.split(sep=';')
     
  # --
  # -- inicio da computação escalar
  # --

  for incident in timebox_data[1: len(timebox_data)-1]:
    incidents = incidents + int(incident)
            
  # --
  # -- fim da computação escalar
  # --

  try: 
    half_hour = int(timebox_data[0])
    
    
    if half_hour == 27:
      incident_by_day[day] = incidents
      day = day + 1
      incidents = 0
      

  except ValueError:
    continue

# -- results

for day in incident_by_day:
  print(f'{day}: {incident_by_day[day]}')

fim = time()
tempo = fim - inicio
print(tempo)





#Substitua o trecho do código do algoritmo que utiliza da **computação escalar** por um que utiliza da **computação vetorial**. Use o pacote NumPy.
#Vamos analisar dados de mobilidade urbana da cidade de São Paulo, usando o pacote Numpy. A base de dados contem a quantidade de acidentes ocorridos na cidade entre 14/12/09 e 18/12/09, das 07:00h ás 20:00h, agregados em intervalos de 30 minutos.

# -- read

df = df.drop(columns=['hour','slowness_traffic_%'])

# -- analytics


  # --
  # -- inicio da computação vetorial
  # --

incidentes_dia_14 = np.sum(np.array(df[0:27]))
incidentes_dia_15 = np.sum(np.array(df[27:54]))
incidentes_dia_16 = np.sum(np.array(df[54:81]))
incidentes_dia_17 = np.sum(np.array(df[81:108]))
incidentes_dia_18 = np.sum(np.array(df[108:135]))
  
  

  # --
  # -- fim da computação vetorial
  # --

# -- results
print(f'\
Incidentes_dia_14: {incidentes_dia_14}\n\
Incidentes_dia_15: {incidentes_dia_15}\n\
Incidentes_dia_16: {incidentes_dia_16}\n\
Incidentes_dia_17: {incidentes_dia_17}\n\
Incidentes_dia_18: {incidentes_dia_18}'
)
