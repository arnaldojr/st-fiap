import streamlit as st

# --------- Funções ---------

# Callback para virar a carta
def flip_card(card_id):
    # Reseta o estado de todas as cartas para False
    for cid in ["card_1", "card_2", "card_3"]:
        st.session_state[f"flipped_{cid}"] = False
    
    # Vira a carta clicada
    st.session_state[f"flipped_{card_id}"] = True

# Função para carregar CSS local
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------- Configurações Iniciais ---------

st.set_page_config(page_title="Jogo de Cartas", page_icon="🃏")

# Carregar o CSS para estilização
local_css("style.css")

# Inicialização do estado das cartas
for cid in ["card_1", "card_2", "card_3"]:
    if f"flipped_{cid}" not in st.session_state:
        st.session_state[f"flipped_{cid}"] = False

# Menu lateral para selecionar a rodada
round_selected = st.sidebar.selectbox("Selecione a Rodada", ["Rodada 1", "Rodada 2", "Rodada 3"])

st.title(f"Desafio de Programação - {round_selected}")

# Dicionário de imagens para cada rodada
images_rounds = {
    "Rodada 1": {
        "card_1": {"front": "card_front2.png", "back": "card_back.png"},
        "card_2": {"front": "card_front3.png", "back": "card_back.png"},
        "card_3": {"front": "card_front4.png", "back": "card_back.png"}
    },
    "Rodada 2": {
        "card_1": {"front": "card_front4.png", "back": "card_back.png"},
        "card_2": {"front": "card_front3.png", "back": "card_back.png"},
        "card_3": {"front": "card_front2.png", "back": "card_back.png"}
    },
    "Rodada 3": {
        "card_1": {"front": "card_front.png", "back": "card_back.png"},
        "card_2": {"front": "card_front2.png", "back": "card_back.png"},
        "card_3": {"front": "card_front3.png", "back": "card_back.png"}
    }
}

# Seleciona as imagens baseadas na rodada escolhida
images = images_rounds[round_selected]

# Criar os cards
cols = st.columns(3)
card_ids = ["card_1", "card_2", "card_3"]

for i, card_id in enumerate(card_ids):
    with cols[i]:
        if st.button("", key=f"flip_{card_id}_{round_selected}"):
            flip_card(card_id)
        if st.session_state.get(f"flipped_{card_id}", False):
            st.image(images[card_id]["back"], use_column_width=True)
        else:
            st.image(images[card_id]["front"], use_column_width=True)

# Adicionar seção de informações no rodapé
st.markdown("---")
st.write("**Jogo de Cartas Interativo - Desenvolvido com Streamlit**")
