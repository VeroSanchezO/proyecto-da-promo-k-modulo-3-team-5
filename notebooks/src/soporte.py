
import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest
from scipy.stats import shapiro, levene
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency
import seaborn as sn
import seaborn as sns
import matplotlib.pyplot as plt

# Gestión de los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")

from src import soporte as sp




def exploratory_data(dataframe, columna_groups): 
    
    """
    Realiza un análisis exploratorio de los datos para una columna categórica específica.

    Esta función imprime información sobre los valores únicos de una columna categórica 
    en el DataFrame proporcionado y muestra estadísticas descriptivas tanto para las 
    columnas numéricas como categóricas, divididas por los grupos en esa columna.

    Parámetros:
    -----------
    dataframe : pandas.DataFrame
        El DataFrame que contiene los datos que se van a analizar.

    Salidas:
    --------
    Esta función no retorna ningún valor. En su lugar, imprime la siguiente información:
    - Los valores únicos de la columna `columna_groups`.
    - Estadísticas descriptivas de las columnas categóricas para cada grupo.
    - Estadísticas descriptivas de las columnas numéricas para cada grupo.
    
    """

    print(f"La columna {columna_groups} tiene las siguientes valores únicos:")
    display(pd.DataFrame(dataframe[columna_groups].value_counts()))    
    

    for categoria in dataframe[columna_groups].unique():
        
        dataframe_filtrado = dataframe[dataframe[columna_groups] == categoria]
    
        print("\n ..................... \n")
        print(f"Los principales estadísticos de las columnas categóricas para el grupo {categoria.upper()} son: ")
        display(dataframe_filtrado.describe(include = "O").T)
        
        print("\n ..................... \n")
        print(f"Los principales estadísticos de las columnas numéricas para el grupo {categoria.upper()} son: ")
        display(dataframe_filtrado.describe().T)