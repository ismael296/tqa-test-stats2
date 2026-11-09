
import streamlit as st
import requests

st.set_page_config(page_title="TQA - Prueba Cito")
st.title("🎾 TQA - Prueba de historial punto a punto")

MATCH_ID = "s365_2026_4891173"

URL = (
    "https://api.citoapi.com/api/v1/tennis/"
    f"matches/{MATCH_ID}/timeline"
)

st.write("Partido: Alex Michelsen vs Yannick Hanfmann")
st.write("Torneo: Stockholm · 9 de noviembre de 2026")

if st.button("Consultar historial del partido"):
    try:
        api_key = st.secrets["CITO_API_KEY"]

        response = requests.get(
            URL,
            headers={"x-api-key": api_key},
            timeout=30
        )

        st.write("Código HTTP:", response.status_code)

        try:
            data = response.json()
            st.json(data)
        except ValueError:
            st.text(response.text)

    except KeyError:
        st.error("No se encuentra CITO_API_KEY en Secrets.")
    except requests.RequestException as error:
        st.error(f"Error de conexión: {error}")
