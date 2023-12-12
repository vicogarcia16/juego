import streamlit as st
import random
import os

st.set_page_config(
        page_title="Juego de piedra, papel o tijeras",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get help': 'https://github.com/vicogarcia16/',
            'About': """##### Disfruta esta aplicación extremadamente divertida! \n
            Creada por Víctor Garcia \n"""
        }
    )

    
opciones = ["piedra", "papel", "tijera"]

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

st.markdown("<h1 style='text-align: center;'>Juego de piedra, papel o tijeras</h1>", unsafe_allow_html=True)
col = st.columns([1, 5, 10, 5.5])
user_option = col[2].selectbox("Elige tu opción", opciones)
colum = st.columns([1, 5, 10])
st.write("")
if colum[2].button("Confirmar selección"):
    computer_option = random.choice(opciones)

    col1, col2, col3, col4 = st.columns([8, 10, 10, 5])
    # Mostrar la imagen del usuario
    col2.image(os.path.join("imagenes", user_option + ".png"), width=150, caption="Tu opción")
    # Mostrar la imagen de la computadora
    col3.image(os.path.join("imagenes", computer_option + ".png"), width=150, caption="Opción de la computadora")
    
    st.markdown("<h2 style='text-align: center;'>Resultado</h2>", unsafe_allow_html=True)
    cols = st.columns([7, 5.2, 7])
    if user_option == computer_option:
        cols[1].warning("## ¡Empate!")
    elif (user_option == "piedra" and computer_option == "tijera") or \
            (user_option == "papel" and computer_option == "piedra") or \
            (user_option == "tijera" and computer_option == "papel"):
        cols[1].success("## ¡Ganaste!")
        st.session_state.user_score += 1
    else:
        cols[1].error("## ¡Perdiste!")
        st.session_state.computer_score += 1
    st.write("")
    
    col1, col2 = st.columns(2)
    col1.markdown("<h5 style='text-align: center;'>Jugador</h5>", unsafe_allow_html=True)
    col2.markdown("<h5 style='text-align: center;'>Computadora</h5>", unsafe_allow_html=True)
    col1.markdown("<h4 style='text-align: center;'>" + str(st.session_state.user_score) + "</h4>", unsafe_allow_html=True)
    col2.markdown("<h4 style='text-align: center;'>" + str(st.session_state.computer_score) + "</h4>", unsafe_allow_html=True)

# Centro del botón
col1, col2, col3 = st.columns([1, 5, 9.8])
with col3:
    if st.button("Reiniciar marcador"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        cols = st.columns([9.5, 5, 5, 5.3])
        with cols[0]:
            st.info("### Marcador reiniciado")
