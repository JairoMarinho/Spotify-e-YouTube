import streamlit as st
import pandas as pd
from pymongo import MongoClient
from config.credentials_loader import load_credentials

st.set_page_config(page_title="Dashboard Spotify", layout="wide")

# Carregar dados do MongoDB
@st.cache_data
def load_data():
    creds = load_credentials()
    client = MongoClient(creds['mongodb']['uri'])
    db = client['media_trends']
    collection = db['spotify_tracks']
    data = list(collection.find({}, {'_id': 0}))
    return pd.DataFrame(data)

df = load_data()

st.title("🎧 Dashboard - Spotify Trends")

if df.empty:
    st.warning("Nenhum dado encontrado no MongoDB.")
else:
    with st.sidebar:
        st.header("Filtros")
        artists = st.multiselect("Artistas", options=df['artist'].unique())
        pop_min = st.slider("Popularidade mínima", 0, 100, 50)

    filtered = df.copy()
    if artists:
        filtered = filtered[filtered['artist'].isin(artists)]
    filtered = filtered[filtered['popularity'] >= pop_min]

    st.metric("Faixas filtradas", len(filtered))
    st.metric("Duração média (min)", round(filtered['duration_ms'].mean() / 60000, 2))
    st.metric("Popularidade média", round(filtered['popularity'].mean(), 2))

    st.bar_chart(filtered.groupby("artist")["popularity"].mean())

    st.subheader("📋 Tabela de Faixas")
    st.dataframe(filtered.sort_values(by="popularity", ascending=False))
