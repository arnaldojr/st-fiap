import streamlit as st

# Função para o flip do card
def flip_card(card_id):
    st.session_state[card_id] = not st.session_state.get(card_id, False)

# estado das cartas
if "card_1" not in st.session_state:
    st.session_state.card_1 = True
if "card_2" not in st.session_state:
    st.session_state.card_2 = True
if "card_3" not in st.session_state:
    st.session_state.card_3 = True

st.title("Desafio de Programação")

# Dicionario de imagens
images = {
    "card_1": {
        True: "card_front2.png",  # Imagem de inicial
        False: "card_back.png"   # Imagem da pergunta
    },
    "card_2": {
        True: "card_front3.png",
        False: "card_back.png"
    },
    "card_3": {
        True: "card_front4.png",
        False: "card_back.png"
    }
}

# cria cards
cols = st.columns(3)
with cols[0]:
    if st.button("", key="flip_card_1"):
        flip_card("card_1")
    st.image(images["card_1"][st.session_state.card_1], use_column_width=True)

with cols[1]:
    if st.button("", key="flip_card_2"):
        flip_card("card_2")
    st.image(images["card_2"][st.session_state.card_2], use_column_width=True)

with cols[2]:
    if st.button("", key="flip_card_3"):
        flip_card("card_3")
    st.image(images["card_3"][st.session_state.card_3], use_column_width=True)
