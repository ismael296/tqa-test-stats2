
import streamlit as st
import requests

st.set_page_config(page_title="TQA - Buscar partidos")
st.title("🎾 TQA - Buscar partidos por superficie")

BASE_URL = "https://api.citoapi.com/api/v1/tennis"

PLAYER_ID = "atp_207989"  # Carlos Alcaraz

def buscar_partidos(surface):
    api_key = st.secrets["CITO_API_KEY"]

    response = requests.get(
        f"{BASE_URL}/matches",
        headers={"x-api-key": api_key},
        params={
            "player_id": PLAYER_ID,
            "surface": surface,
            "page": 1,
            "page_size": 10,
            "include": "stats"
        },
        timeout=30
    )

    st.write("Código HTTP:", response.status_code)
    response.raise_for_status()
    return response.json()

if st.button("Buscar partidos en tierra batida"):
    try:
        data = buscar_partidos("Clay")
        st.json(data)
    except Exception as e:
        st.error(str(e))

if st.button("Buscar partidos en pista dura"):
    try:
        data = buscar_partidos("Hard")
        st.json(data)
    except Exception as e:
        st.error(str(e))

