import streamlit as st
import pandas as pd

st.title("Tableau de Données Iris")
fichier = st.file_uploader("Uploadez le fichier CSV", type="csv")

if fichier:
    df = pd.read_csv(fichier)
  
    st.write("### Aperçu des données")
    st.dataframe(df)

    colonnes = df.iloc[:, :5]  
    st.write("### Graphique à barres")
    st.bar_chart(colonnes)

    st.write("### Graphique en ligne")
    st.line_chart(colonnes)
else:
    st.info("Veuillez uploader un fichier CSV pour afficher les données.")
