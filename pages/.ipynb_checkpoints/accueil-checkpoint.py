import streamlit as st





st.title("🏡 Bienvenue sur l'application d'Estimation Immobilière")

st.markdown("""
Cette application vous permet d'obtenir une **estimation du prix d'un bien immobilier**
et d'explorer les **biens actuellement en vente** sur une carte interactive.

Sélectionnez une page dans le menu situé à gauche pour commencer.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Estimation")
    st.write(
        """
        Estimez la valeur de votre bien immobilier en renseignant ses caractéristiques :

        - 📍 Localisation
        - 📐 Surface
        - 🛏️ Nombre de pièces
        - 🏠 Type de bien
        - 📅 Autres informations utiles

        Notre modèle de Machine Learning calcule une estimation du prix à partir des données saisies.
        """
    )

    if st.button("Accéder à l'estimation"):
        st.switch_page("pages/estimation.py")  # Adapter le nom du fichier

with col2:
    st.subheader("🗺️ Carte des biens en vente")
    st.write(
        """
        Consultez les biens immobiliers actuellement en vente grâce à une carte interactive.

        Vous pouvez :

        - 📍 Localiser les annonces
        - 💰 Comparer les prix
        - 🏘️ Explorer différents quartiers
        - 🔎 Analyser le marché immobilier
        """
    )

    if st.button("Voir la carte"):
        st.switch_page("pages/carte.py")  # Adapter le nom du fichier

st.divider()

st.info(
    """
    💡 **Objectif de l'application**

    Cette application combine un modèle de prédiction et une visualisation cartographique
    afin d'aider les utilisateurs à estimer un bien immobilier et à le comparer avec les
    annonces actuellement disponibles sur le marché.
    """
)

st.markdown("---")

st.caption("Développé en Python • Streamlit • Machine Learning")