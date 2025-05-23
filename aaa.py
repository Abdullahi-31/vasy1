import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import seaborn as sns

link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/flights.csv'
df = pd.read_csv(link)

st.title("Manipulation des données et création de graphiques")

line = df
year = df['year']
month = df['month']
flight = df
st.selectbox("Quel dataset veux-tu utiliser ?", "flight")
st.dataframe(flight.head())

colonneX = st.selectbox("Choisisez la data pour l'axe X", flight.columns)
colonneY = st.selectbox("Choisisez la data pour l'axe Y", flight.columns)


graph = ['line_chart','scatter_chart','bar_chart']
choix_gr = st.selectbox("Choisisez le graphique",graph)
if choix_gr == "line_chart":
    st.line_chart(line, x=f'{colonneX}', y=f'{colonneY}')
elif choix_gr == "scatter_chart":
    st.scatter_chart(line, x=f'{colonneX}', y=f'{colonneY}', size='passengers')
elif choix_gr == "bar_chart":
    st.bar_chart(line, x=f'{colonneX}', y=f'{colonneY}')

agree = st.checkbox("Afficher la matrice de corélation")
if agree:
    corr = df.corr(numeric_only=True)
    st.pyplot(sns.heatmap(corr, annot=True).get_figure())