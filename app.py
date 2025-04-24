import streamlit as st
from datetime import date
from predictor import predict_emotion

# Configurar la página con favicon y título
st.set_page_config(
    page_title="SentIA",
    page_icon="logo.png", 
    layout="centered"
)

# Estilos personalizados (colores, botón, etc.)
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f8f8ff, #805ad5);
        }
        .stTextInput>div>div>input {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #805ad5;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-weight: bold;
        }
        h1 {
            color: #805ad5;
            font-family: 'Segoe UI', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Logo y título
st.image("logo.png", width=100) 
st.markdown("<h1 style='text-align: center;'>SentIA</h1>", unsafe_allow_html=True)

# Fecha actual
fecha_actual = date.today().strftime("%d/%m/%Y")
st.markdown(f"<h4 style='text-align: center;'>Fecha: {fecha_actual}</h4>", unsafe_allow_html=True)

# Entrada de texto
user_input = st.text_area("Describe cómo te has sentido hoy", height=200)

# Botón y predicción
if st.button("Aceptar"):
    if user_input.strip() == "":
        st.warning("Por favor, escribe algo primero.")
    else:
        emocion = predict_emotion(user_input)
        st.success(f"🧠 Emoción detectada: **{emocion.upper()}**")
