
import streamlit as st
import requests

st.set_page_config(page_title="TQA - Prueba Clay")
st.title("🎾 TQA - Historial punto a punto")

MATCH_ID = "atp_2026_0425_370"

URL = (
    "https://api.citoapi.com/api/v1/tennis/"
    f"matches/{MATCH_ID}/timeline"
)

if st.button("Consultar historial del partido"):
    try:
        api_key = st.secrets["CITO_API_KEY"]

        response = requests.get(
            URL,
            headers={"x-api-key": api_key},
            timeout=30
        )

        st.write("Código HTTP:", response.status_code)
        response.raise_for_status()
        st.json(response.json())

    except Exception as error:
        st.error(str(error))


