import streamlit as st

# Função para o flip do card
def flip_card(card_id):
    if st.session_state['selected_card'] == card_id:
        st.session_state['selected_card'] = None  # Reseta para o estado inicial
    else:
        st.session_state['selected_card'] = card_id

# Inicialização do estado das cartas
if "selected_card" not in st.session_state:
    st.session_state.selected_card = None

st.title("Desafio de Programação")

# Dicionário de imagens
images = {
    "card_1": {
        "front": "card_front2.png",  # Imagem inicial
        "back": "card_back.png"      # Imagem da pergunta
    },
    "card_2": {
        "front": "card_front3.png",
        "back": "card_back.png"
    },
    "card_3": {
        "front": "card_front4.png",
        "back": "card_back.png"
    }
}

# Criar os cards
cols = st.columns(3)
with cols[0]:
    if st.button("pergunta1", key="flip_card_1"):
        flip_card("card_1")
    if st.session_state.selected_card == "card_1":
        st.image(images["card_1"]["back"], use_column_width=True)
    elif st.session_state.selected_card is None:
        st.image(images["card_1"]["front"], use_column_width=True)
    else:
        st.empty()

with cols[1]:
    if st.button("pergunta2", key="flip_card_2"):
        flip_card("card_2")
    if st.session_state.selected_card == "card_2":
        st.image(images["card_2"]["back"], use_column_width=True)
    elif st.session_state.selected_card is None:
        st.image(images["card_2"]["front"], use_column_width=True)
    else:
        st.empty()

with cols[2]:
    if st.button("pergunta3", key="flip_card_3"):
        flip_card("card_3")
    if st.session_state.selected_card == "card_3":
        st.image(images["card_3"]["back"], use_column_width=True)
    elif st.session_state.selected_card is None:
        st.image(images["card_3"]["front"], use_column_width=True)
    else:
        st.empty()
