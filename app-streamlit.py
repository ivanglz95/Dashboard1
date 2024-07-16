import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

######################
#Configuracion de pagina
#titulos
#iconos
#diseño de la barra lateral
st.set_page_config (
    page_title = "Panel de control"
    page_icon = "",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

#######################
#CSS styling
st.markdown ("""
<style>
</style>                     
""", unsafe_allow_html=True)

######################
#DATA
#Proceso de transformacion  de los datos
df= pd.read_excel("")
df["Columna_valores"] = df[""].apply(lambda x:float(x.replace(".","")).replace(",","."))

df["fecha"] = pd.to_datetime(df["fecha"], format = "%d/%m/%Y")
df_sorted = df.sort_values ("fecha")

#Sidebar
with st.sidebar:
    st.title("Oeste Hogar Dashboard")
    #Seleccionar años
    df["fecha"].dt.year.unique()
    years_unique = df["fecha_envio"].dt.year.unique()
    year_list = list (map(str, years_unique))
    selected_year = 2024
    selected_year = st.selectbok ("Seleccione un año",year_list)
    df_selected_year = df[df["fecha"].dt.year==int(selected_year)]

###########################
#visualizaciones
#Copiamos los graficos hechos

#1
def make_fig (data):
    fig =
    return fig

##########################
#Dashboard Main panel
#definimos el tamaño de nuestras columnas
col = st.column (())