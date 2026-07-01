import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium







df = pd.read_csv("data_geoloc.csv")
st.title("Carte des annonces")

def display_map():
    
    carte = folium.Map(location=[48.857, 2.35], zoom_start=12)
    for _, r in df.iterrows():
        popup = (f"<b>{r['type_bien']}</b><br>"
                 f"Prix : {r['prix_eur']:,.0f} €<br>".replace(",", " ") +
                 f"Surface : {r['surface_m2']} m²<br>"
                 f"Pièces : {r['nb_pieces']}<br>"
                 f"DPE : {r['dpe']}<br>"
                 f"{r['adresse']}<br>"
                 f"<a href='{r['url']}' target='_blank'>Voir l'annonce</a>")
        
        folium.Marker(
            [r["latitude"], r["longitude"]],
            popup=folium.Popup(popup, max_width=300),
            tooltip=f"{r['prix_eur']:,.0f} €".replace(",", " ")
        ).add_to(carte)

    st_folium(carte, width=1000, height=600)


display_map()