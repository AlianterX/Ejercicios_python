'''
PRUEBA EVALUACIÓN  CURSO 25-26 
Ejercicio 1 

La prueba de tolerancia  a la  glucosa, también conocida como «examen de tolerancia oral a la glucosa»,
mide la respuesta del cuerpo al azúcar (glucosa). Esta prueba se puede usar como prueba de detección para la diabetes de tipo 2.
En el departamento de investigación de un hospital se está realizando un estudio para conocer si la tolerancia a la glucosa en 
pacientes sanos tiende a decrecer a medida que la edad de la persona aumenta, es decir tarda más tiempo en desaparecer en nuestro
organismo conforme envejecemos. Para obtener las conclusiones del estudio se suministra una dosis de glucosa, en forma de un preparado
via oral, a dos muestras de pacientes sanos escogidos al azar, jovenes( edad menor de 30) y otros adultos ( edad superior a 30). 
Consideraremos estas muestras independientes. El test consistió en realizar la medición de glucosa en sangre en el momento de la toma
( nivel basal ) de 100 gramos de glucosa y a los 60 minutos de la toma. Los resultados se muestran en el Excel.
En la primera columna se representa con 1 a los pacientes cuyo rango de edad es menor que 30 ( jóvenes) y con 2 a los pacientes cuyo
rango de edad es mayor que 30, en la segunda columna la concentración en sangre en el momento de la toma ( nivel basal, en mg/Dl) y
en la tercera columna la concentración de glucosa pasada una hora de la ingesta de la pastilla en mg/Dl


'''

'''
a) Obtener las medidas de centralización y dispersión para cada uno de los dos grupos de control 
para el nivel de glucosa basal, especificando para cada uno de los casos si la media es o no representativa.
'''
import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt 

print("\n Ejercicio 1 \n a)")
# Cargar los datos desde el archivo Excel
path = "EVALMASTER.xlsx"
df = pd.read_excel(path)
print(df)
# Dividir los datos en dos grupos según la edad
grupo_jovenes = df[df['Grupo de control'] == 1]['Nivel glucosa basal']
grupo_jovenes_60min = df[df['Grupo de control'] == 1]['Nivel glucosa 60 min']
grupo_adultos = df[df['Grupo de control'] == 2]['Nivel glucosa basal']
grupo_adultos_60min = df[df['Grupo de control'] == 2]['Nivel glucosa 60 min']

# Calcular medidas de centralización y dispersión para el grupo de jóvenes y adultos (media, mediana, moda, rango, varianza, desviación estándar y coeficiente de variacion)
def medidas_estadisticas(grupo, nombre_grupo):
    media = grupo.mean()
    mediana = grupo.median()
    moda = grupo.mode()[0]  # En caso de múltiples modas, tomar la primera
    rango = grupo.max() - grupo.min()
    varianza = grupo.var()
    desviacion_estandar = grupo.std()
    coeficiente_variacion = desviacion_estandar / media
    
    print(f"\nMedidas estadísticas para {nombre_grupo}:")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Rango: {rango}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_estandar}")
    print(f"Coeficiente de variación: {coeficiente_variacion}")

    if coeficiente_variacion < 0.3:
        print("La media es representativa.")
    else:
        print("La media no es representativa.")
    


medidas_estadisticas(grupo_jovenes, "Grupo de jóvenes (Nivel glucosa basal)")
medidas_estadisticas(grupo_adultos, "Grupo de adultos (Nivel glucosa basal)")


'''
b)	Estudiar la simetría y la curtosis del nivel de glucosa basal en los adultos ( grupo de control 2)

'''

print("\n b)")

# Cálculo de asimetría y curtosis para el grupo de adultos
asimetria_adultos = stats.skew(grupo_adultos)
curtosis_adultos = stats.kurtosis(grupo_adultos)
print(f"\nAsimetría del nivel de glucosa basal en adultos: {asimetria_adultos}")
print(f"Curtosis del nivel de glucosa basal en adultos: {curtosis_adultos}")


# Interpretación de la asimetría y curtosis
if asimetria_adultos > 0:
    print("La distribución es asimétrica positiva (sesgada a la derecha).") 
elif asimetria_adultos < 0:
    print("La distribución es asimétrica negativa (sesgada a la izquierda).")
else:
    print("La distribución es simétrica.")

if curtosis_adultos > 3:
    print("La distribución es leptocúrtica ")
elif curtosis_adultos < 3:
    print("La distribución es platicúrtica ")
else:
    print("La distribución es mesocúrtica ")


'''
c)	Indicar para cada una de las variables de estudio (nivel glucosa basal y nivel glucosa pasados 60 min) y en el grupo de control 1 el valor de los cuartiles y 
su significado y obtener el box- plot ( diagrama de cajas) correspondiente. Estudiar la presencia de valores atípicos.

'''    
print("\n c)")
# Calcular cuartiles para el grupo de jóvenes (grupo de control 1)
cuartiles_jovenes_basal = grupo_jovenes.quantile([0.25, 0.5, 0.75])
cuartiles_jovenes_60min = grupo_jovenes_60min.quantile([0.25, 0.5, 0.75])
print(f"\nCuartiles del nivel de glucosa basal en jóvenes:\n{cuartiles_jovenes_basal}")
print(f"\nCuartiles del nivel de glucosa a los 60 min en jóvenes:\n{cuartiles_jovenes_60min}")

# Significado de los cuartiles
print("\nSignificado de los cuartiles:")
print("Q1 (25%): El 25% de los valores están por debajo de este valor.")
print("Q2 (50%): La mediana, el 50% de los valores están por debajo de este valor.")
print("Q3 (75%): El 75% de los valores están por debajo de este valor.")

# Box-plot para el nivel de glucosa basal en jóvenes
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(grupo_jovenes, vert=True, patch_artist=True)
plt.title('Box-plot del nivel de glucosa basal en jóvenes')
plt.ylabel('Nivel de glucosa basal (mg/Dl)')
# Box-plot para el nivel de glucosa a los 60 min en jóvenes
plt.subplot(1, 2, 2)
plt.boxplot(df[df['Grupo de control'] == 1]['Nivel glucosa 60 min'], vert=True, patch_artist=True)
plt.title('Box-plot del nivel de glucosa a los 60 min en jóvenes')  
plt.ylabel('Nivel de glucosa a los 60 min (mg/Dl)')
plt.tight_layout()
plt.show()
print("\nVemos en los diagramas de bigote que hay valores atipicos en los niveles de glucosa en 60 min.")

# Estudio de valores atípicos para el nivel de glucosa basal en jóvenes
Q1 = cuartiles_jovenes_basal[0.25]
Q3 = cuartiles_jovenes_basal[0.75]  
RIC = Q3 - Q1
limite_inferior = Q1 - 1.5 * RIC
limite_superior = Q3 + 1.5 * RIC
valores_atipicos_basal = grupo_jovenes[(grupo_jovenes < limite_inferior) | (grupo_jovenes > limite_superior)] 

if valores_atipicos_basal.empty:
    print("\nNo hay valores atípicos en el nivel de glucosa basal en jóvenes.")
else:    
    print(f"\nValores atípicos en el nivel de glucosa basal en jóvenes:\n{valores_atipicos_basal}")

# Estudio de valores atípicos para el nivel de glucosa a los 60 min en jóvenes
Q1_60min = cuartiles_jovenes_60min[0.25]
Q3_60min = cuartiles_jovenes_60min[0.75]  
RIC_60min = Q3_60min - Q1_60min 
limite_inferior_60min = Q1_60min - 1.5 * RIC_60min
limite_superior_60min = Q3_60min + 1.5 * RIC_60min
valores_atipicos_60min = grupo_jovenes_60min[(grupo_jovenes_60min < limite_inferior_60min) | (grupo_jovenes_60min > limite_superior_60min)]
print(f"\nValores atípicos en el nivel de glucosa a los 60 min en jóvenes:\n{valores_atipicos_60min}")

'''
d)	Estudiar la normalidad de los datos de cada uno de los grupos de control estudiados para el nivel de glucosa pasados 60 minutos. 

'''
print("\n d)")
# Para ver la normalidad vamos a usar un grafico Q-Q 

# Gráfico Q-Q para el grupo de jóvenes (grupo de control 1)
plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1)
stats.probplot(grupo_jovenes_60min, dist="norm", plot=plt)
plt.title('Gráfico Q-Q del nivel de glucosa a los 60 min en jóvenes')

# Gráfico Q-Q para el grupo de adultos (grupo de control 2)
plt.subplot(1, 2, 2)   
stats.probplot(grupo_adultos_60min, dist="norm", plot=plt)
plt.title('Gráfico Q-Q del nivel de glucosa a los 60 min en adultos')
plt.tight_layout()
plt.show()
# Interpretación visual
print("\nInterpretación visual de los gráficos Q-Q:")
print("Los puntos siguen aproximadamente una línea recta, luego los datos se distribuyen normalmente en ambos grupos.")

# Prueba de normalidad de Shapiro-Wilk para el grupo de jóvenes
stat_jovenes, p_jovenes = stats.shapiro(grupo_jovenes_60min)
print(f"\nPrueba de normalidad de Shapiro-Wilk para jóvenes: estadístico={stat_jovenes}, p-valor={p_jovenes}")
if p_jovenes > 0.05:
    print("No se rechaza la hipótesis nula: los datos siguen una distribución normal.") 
else:
    print("Se rechaza la hipótesis nula: los datos no siguen una distribución normal.")

# Prueba de normalidad de Shapiro-Wilk para el grupo de adultos
stat_adultos, p_adultos = stats.shapiro(grupo_adultos_60min)
print(f"\nPrueba de normalidad de Shapiro-Wilk para adultos: estadístico={stat_adultos}, p-valor={p_adultos}")
if p_adultos > 0.05:
    print("No se rechaza la hipótesis nula: los datos siguen una distribución normal.") 
else:
    print("Se rechaza la hipótesis nula: los datos no siguen una distribución normal.")

# Coclusión sobre la normalidad
print("\nConclusión sobre la normalidad:")
print("Ambos grupos siguen una distribución normal.")   

'''
Ejercicio 2

Se quiere ahora estudiar la relación existente entre el nivel basal y el nivel de glucosa que tienen los pacientes
sanos jóvenes( grupo 1) una hora después de tomar el preparado de glucosa. Se pide:

'''

'''
a) Estudiar la relación lineal existente entre estas dos variables de estudio gráficamente y mediante algún valor estadístico de forma razonada.

'''
print("\n Ejercicio 2 \n a)")
# Gráfico de dispersión entre el nivel de glucosa basal y el nivel de glucosa a los 60 min en jóvenes
plt.figure(figsize=(7, 5))
plt.scatter(grupo_jovenes, grupo_jovenes_60min, color='blue', alpha=0.7)
plt.title('Gráfico de dispersión: Nivel de glucosa basal vs Nivel de glucosa a los 60 min en jóvenes')
plt.xlabel('Nivel de glucosa basal (mg/Dl)')    
plt.ylabel('Nivel de glucosa a los 60 min (mg/Dl)')
plt.grid()
plt.show()
print("\nInterpretación del gráfico de dispersión:")
print("Se observa una relacion positiva entre el nivel de glucosa basal y el nivel de glucosa a los 60 min en jóvenes.")

# Cálculo del covarianza y el coeficiente de correlación
covarianza = np.cov(grupo_jovenes, grupo_jovenes_60min)[0][1]
print(f"\nCovarianza entre el nivel de glucosa basal y el nivel de glucosa a los 60 min en jóvenes: {covarianza}")
print("la covarianza es positiva, lo que indica una relación lineal positiva entre las dos variables.")
correlacion, p_valor = stats.pearsonr(grupo_jovenes, grupo_jovenes_60min)
print(f"\nCoeficiente de correlación entre el nivel de glucosa basal y el nivel de glucosa a los 60 min en jóvenes: {correlacion}")
print(f"como el coeficiente de correlación es {correlacion:4f},que esta cerca de 0.8, las variables tienen una relacion alta.")

'''
b) Obtener un modelo lineal que explica el nivel de glucosa en sangre a los 60 minutos en función del nivel basal del paciente
y realizar la estimación para un paciente cuyo nivel basal es 83 mg/Dl

'''
print("\n b)")
# Ajuste de un modelo de regresión lineal
# Y = nivel de glucosa a los 60 min
# X = nivel de glucosa basal
# Y = aX + b
pendiente, intercepcion, r_value, p_value, std_err = stats.linregress(grupo_jovenes, grupo_jovenes_60min)
print(f"\nModelo de regresión lineal: Nivel glucosa 60 min = {pendiente} * Nivel glucosa basal + {intercepcion}")

# Estimación para un paciente con nivel basal de 83 mg/Dl
nivel_basal_estimar = 83
nivel_60min_estimado = pendiente * nivel_basal_estimar + intercepcion  
print(f"\nEstimación del nivel de glucosa a los 60 min para un paciente con nivel basal de {nivel_basal_estimar} mg/Dl: {nivel_60min_estimado} mg/Dl")  

'''
c)¿Qué tanto por ciento del nivel de glucosa en sangre pasados 60 minutos queda no queda explicado por el anterior modelo?

'''
print("\n c)")

# Cálculo del coeficiente de determinación R^2
R_squared = r_value**2 # Como estamos en una regresion lineal, es el cuadrado del coeficiente de correlación
porcentaje_no_explicado = (1 - R_squared) * 100
print(f"\nPorcentaje del nivel de glucosa a los 60 min no explicado por el modelo: {porcentaje_no_explicado}%")
print("El porcentaje del nivel de glucosa a los 60 min no explicado por el modelo es bajo, lo que indica que el modelo es adecuado para explicar la relación entre las dos variables.")

'''
d)	Si aumentásemos el nivel basal de un paciente en 5 mg/Dl ¿Qué variación experimentaría su nivel de glucosa al cabo de 60 minutos?

'''

print("\n d)")
# Cálculo de la variación en el nivel de glucosa a los 60 min al aumentar el nivel basal en 5 mg/Dl
aumento_nivel_basal = 5
variacion_nivel_60min = pendiente * aumento_nivel_basal 
print(f"\nVariación en el nivel de glucosa a los 60 min al aumentar el nivel basal en {aumento_nivel_basal} mg/Dl: {variacion_nivel_60min} mg/Dl")

'''
Ejercicio 3 
a) Se quiere estudiar si se puede admitir que el nivel medio de glucosa en sangre en el momento de la ingestión en los jóvenes es 88 mg/Dl.
Obtener el intervalo de confianza al 95% y al 99% para el nivel medio de glucosa en sangre de los jóvenes y posteriormente contesta a la
cuestión planteada con los resultados obtenidos o con un contraste de hipótesis.

'''
print("\n Ejercicio 3 \n a)")
# Veamos primero las hipótesis
# H0: nivel medio de glucosa en sangre en jóvenes = 88 mg/Dl
# H1: nivel medio de glucosa en sangre en jóvenes != 88 mg/Dl

# Vamos primero a calcular los intervalos de confianza y despues veremos si 88 mg/Dl esta dentro del intervalo de confianza

# Intervalo de confianza al 95%
nivel_confianza_95 = 0.05
n_jovenes = len(grupo_jovenes) 
media_jovenes = grupo_jovenes.mean()
std_jovenes = grupo_jovenes.std(ddof=1) # Desviación estándar muestral
error_estandar = std_jovenes / np.sqrt(n_jovenes)
t_critico_95 = stats.t.ppf((1 + nivel_confianza_95) / 2, df=n_jovenes - 1)
margen_error_95 = t_critico_95 * error_estandar 
print(margen_error_95)

intervalo_confianza_95 = (media_jovenes - margen_error_95, media_jovenes + margen_error_95)
print(f"\nIntervalo de confianza al 95% para el nivel medio de glucosa en sangre en jóvenes: {intervalo_confianza_95}")

# Intervalo de confianza al 99%
nivel_confianza_99 = 0.99
t_critico_99 = stats.t.ppf((1 + nivel_confianza_99) / 2, df=n_jovenes - 1)
margen_error_99 = t_critico_99 * error_estandar
intervalo_confianza_99 = (media_jovenes - margen_error_99, media_jovenes + margen_error_99)
print(f"\nIntervalo de confianza al 99% para el nivel medio de glucosa en sangre en jóvenes: {intervalo_confianza_99}")

# Veamos si 88 mg/Dl esta dentro de los intervalos de confianza
if intervalo_confianza_95[0] <= 88 <= intervalo_confianza_95[1]:
    print("\nAl 95% de confianza, se puede admitir que el nivel medio de glucosa en sangre en jóvenes es 88 mg/Dl.")
else:
    print("\nAl 95% de confianza, no se puede admitir que el nivel medio de glucosa en sangre en jóvenes sea 88 mg/Dl.")

if intervalo_confianza_99[0] <= 88 <= intervalo_confianza_99[1]:
    print("\nAl 99% de confianza, se puede admitir que el nivel medio de glucosa en sangre en jóvenes es 88 mg/Dl.")
else:
    print("\nAl 99% de confianza, no se puede admitir que el nivel medio de glucosa en sangre en jóvenes sea 88 mg/Dl.")  

'''

b) Obtener los intervalos de confianza al 95%  para la diferencia de medias en el nivel basal de glucosa entre adultos y jovenes
e interpreta los resultados. ¿Se puede concluir que el nivel basal de glucosa de los jóvenes y los adultos es el mismo con nivel
de significación del 5%? .Suponiendo que se cumplen las condiciones iniciales teóricas para obtener los intervalos de confianza

'''
print("\n b)")
# Cálculo del intervalo de confianza para la diferencia de medias entre adultos y jóvenes
nivel_confianza = 0.95
n_adultos = len(grupo_adultos)
media_adultos = grupo_adultos.mean()
std_adultos = grupo_adultos.std(ddof=1) # Desviación estándar muestral
error_estandar_diff = np.sqrt((std_jovenes**2 / n_jovenes) + (std_adultos**2 / n_adultos))
t_critico = stats.t.ppf((1 + nivel_confianza) / 2, df=min(n_jovenes - 1, n_adultos - 1))
margen_error_diff = t_critico * error_estandar_diff
diferencia_medias = media_jovenes - media_adultos
intervalo_confianza_diff = (diferencia_medias - margen_error_diff, diferencia_medias + margen_error_diff)
print(f"\nIntervalo de confianza al 95% para la diferencia de medias entre adultos y jóvenes: {intervalo_confianza_diff}")

# Interpretación del intervalo de confianza
print("\nInterpretación del intervalo de confianza:")   
if intervalo_confianza_diff[0] <= 0 <= intervalo_confianza_diff[1]:
    print("No se puede concluir que el nivel basal de glucosa de los jóvenes y los adultos sea diferente al nivel de significación del 5%.")
else:
    print("Se puede concluir que el nivel basal de glucosa de los jóvenes y los adultos es diferente al nivel de significación del 5%.")

'''
c) Se quiere estudiar la proporción de la población con un nivel basal de glucosa superior a 95 mg/Dl (prediabetes). A partir de la muestra del fichero
(tomando todos los datos) obtener un intervalo de confianza al 98% y contrastar la hipótesis que la proporción de la población con glucosa superior a 95 mg/Dl
es 0,15 con nivel de significación del 5%.

'''
print("\n c)")
# Veamos primero las hipótesis
# H0: p = 0.15
# H1: p != 0.15

# Cálculo de la proporción muestral
total_pacientes = len(df)
pacientes_pre_diabetes = len(df[df['Nivel glucosa basal'] > 95])
proporcion_muestral = pacientes_pre_diabetes / total_pacientes
print(f"\nProporción muestral de pacientes con nivel basal de glucosa superior a 95 mg/Dl: {proporcion_muestral}")

# Cálculo del intervalo de confianza al 98%
nivel_confianza_98 = 0.98
z_critico_98 = stats.norm.ppf((1 + nivel_confianza_98) / 2)
error_estandar_proporcion = np.sqrt((proporcion_muestral * (1 - proporcion_muestral)) / total_pacientes)
margen_error_proporcion = z_critico_98 * error_estandar_proporcion
intervalo_confianza_proporcion = (proporcion_muestral - margen_error_proporcion, proporcion_muestral + margen_error_proporcion)
print(f"\nIntervalo de confianza al 98% para la proporción de pacientes con nivel basal de glucosa superior a 95 mg/Dl: {intervalo_confianza_proporcion}")

# Contraste de hipótesis
p_0 = 0.15
z_estadistico = (proporcion_muestral - p_0) / error_estandar_proporcion
p_valor = 2 * (1 - stats.norm.cdf(abs(z_estadistico)))
print(f"\nEstadístico z: {z_estadistico}, p-valor: {p_valor}")
if p_valor > 0.05:
    print("No se rechaza la hipótesis nula: la proporción de la población con glucosa superior a 95 mg/Dl es 0.15.")
else:
    print("Se rechaza la hipótesis nula: la proporción de la población con glucosa superior a 95 mg/Dl no es 0.15.")

'''
d)¿Se detecta una variación significativa del nivel de glucosa en sangre en el grupo de los adultos después de la toma ? 

'''
print("\n d)")
# Veamos primero las hipótesis
# H0: media_diferencias = 0 (no hay variación significativa)
# H1: media_diferencias != 0 (hay variación significativa)

# Cálculo de las diferencias entre el nivel basal y el nivel a los 60 min en adultos
diferencias_adultos = grupo_adultos_60min - grupo_adultos
media_diferencias = diferencias_adultos.mean()
std_diferencias = diferencias_adultos.std(ddof=1)
n_diferencias = len(diferencias_adultos)
error_estandar_diferencias = std_diferencias / np.sqrt(n_diferencias)
t_estadistico_diferencias = media_diferencias / error_estandar_diferencias
p_valor_diferencias = 2 * (1 - stats.t.cdf(abs(t_estadistico_diferencias), df=n_diferencias - 1))
print(f"\nEstadístico t: {t_estadistico_diferencias}, p-valor: {p_valor_diferencias}")
if p_valor_diferencias > 0.05:
    print("No se rechaza la hipótesis nula: no hay una variación significativa del nivel de glucosa en sangre en el grupo de adultos después de la toma.")
else:
    print("Se rechaza la hipótesis nula: hay una variación significativa del nivel de glucosa en sangre en el grupo de adultos después de la toma.")


