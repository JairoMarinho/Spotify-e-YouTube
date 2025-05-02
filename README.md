# Spotify-e-YouTube

# 🎧📺 Spotify e YouTube - Análise Integrada de Tendências Musicais e Audiovisuais

Projeto desenvolvido para a disciplina de **Big Data** no **SENAC Pernambuco**, com o objetivo de construir um pipeline **ETL** integrando dados das APIs do **Spotify** e **YouTube**, realizando análises cruzadas e visualização de tendências musicais e audiovisuais.

---

## ✅ Funcionalidades

- 🔍 Extração de dados de playlists, faixas e artistas do Spotify
- 📺 Extração de dados de vídeos populares do YouTube (planejado)
- 🧹 Transformação dos dados: limpeza, padronização e cálculo de métricas
- ☁️ Armazenamento em **MongoDB Atlas**
- 📊 Visualização interativa com **Streamlit**
- 🔐 Gerenciamento seguro de credenciais via `credentials.json`

---

## 🧱 Estrutura do Projeto

spotify_youtube_etl/ ├── config/ │ ├── credentials.json # Armazena as chaves da API (não versionar!) │ └── credentials_loader.py # Função para carregar credenciais ├── etl/ │ ├── spotify_etl.py # Extração de dados do Spotify │ └── transform.py # Transformação e limpeza dos dados ├── load/ │ └── to_mongodb.py # Inserção de dados no MongoDB ├── dashboard/ │ └── dashboard.py # Dashboard interativo com Streamlit ├── main.py # Script principal que orquestra o ETL ├── requirements.txt # Dependências do projeto └── README.md

📦 Tecnologias Utilizadas
Python 3.x

Spotipy – Spotify Web API

Google API Client – YouTube API (em desenvolvimento)

MongoDB Atlas – Armazenamento na nuvem

Pandas – Manipulação de dados

Streamlit – Dashboard interativo

Requests / SSL – Integrações com APIs seguras


🧠 Objetivos Acadêmicos
Aplicar um pipeline ETL real com múltiplas fontes de dados

Integrar APIs REST com autenticação

Armazenar e consultar dados em banco NoSQL

Construir visualizações úteis para tomada de decisão
