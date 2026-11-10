
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

import streamlit as st
import requests

st.set_page_config(page_title="TQA - Prueba timeline")
st.title("🎾 TQA - Prueba timeline en tierra batida")

MATCH_ID = "atp_2026_0410_372"

URL = (
    "https://api.citoapi.com/api/v1/tennis/"
    f"matches/{MATCH_ID}/timeline"
)

if st.button("Consultar timeline"):
    try:
        api_key = st.secrets["CITO_API_KEY"]

        response = requests.get(
            URL,
            headers={"x-api-key": api_key},
            timeout=30
        )

        st.write("Código HTTP:", response.status_code)
        response.raise_for_status()

        data = response.json()

        st.write("Granularidad:", data.get("granularity"))
        st.write("Cobertura:", data.get("coverage"))
        st.write("Eventos:", len(data.get("events", [])))

        st.json(data)

    except Exception as error:
        st.error(str(error))


import streamlit as st
import requests

st.title("TQA - Control de API")

if st.button("Consultar consumo de Cito"):
    try:
        response = requests.get(
            "https://api.citoapi.com/api/v1/health",
            headers={
                "x-api-key": st.secrets["CITO_API_KEY"]
            },
            timeout=30
        )

        st.write("HTTP:", response.status_code)
        st.json(response.json())

    except Exception as error:
        st.error(str(error))
