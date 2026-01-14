import streamlit as st 
from fruit_manager import *

st.title("🍎 Dashboard de la Plantation")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

with st.sidebar:
    st.header("Vendre des fruits")
    fruit_vendre = st.selectbox("chsoisir un fruit", list(inventaire.keys()))
    quantite_vendre = st.number_input("quantité à vendre", min_value=1, step=1)
    
    if st.button("Vendre"):
        inventaire,tresorerie = vendre(inventaire, fruit_vendre, quantite_vendre, tresorerie, prix)
        

st.header(" 💰 Trésorerie")
st.metric("Montant disponible", value=f"{tresorerie:.2f} $")

st.header(" Inventaire")
st.table(inventaire)