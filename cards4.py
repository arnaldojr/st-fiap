import streamlit as st

# --------- Funções ---------

# Callback para virar a carta
def flip_card(card_id):
    # Verifica o estado atual da carta
    current_state = st.session_state.get(f"flipped_{card_id}", False)
    
    # Vira ou desvira a carta clicada
    st.session_state[f"flipped_{card_id}"] = not current_state

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

st.title(f"NEXT FIAP - {round_selected}")

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
            # Mostrar o desafio para o usuário
            st.write("### Desafio:")
            st.write("Escreva uma função em Python que calcule o fatorial de 5! dividido por 6!")
            st.code("def calcular_fatorial_divisao():\n    # Escreva seu código aqui", language="python")
            user_code = st.text_area("Insira seu código abaixo e clique em 'Executar'", height=200)
            if st.button("Executar código"):
                try:
                    # Variáveis auxiliares
                    local_variables = {}
                    # Executa o código do usuário
                    exec(user_code, {}, local_variables)
                    # Verifica se a função foi definida
                    if "calcular_fatorial_divisao" in local_variables:
                        # Executa a função e verifica o resultado
                        result = local_variables["calcular_fatorial_divisao"]()
                        if result == 1/6:  # O resultado correto de 5!/6! é 1/6
                            st.success("Parabéns! Você acertou!")
                        else:
                            st.error("O resultado está incorreto. Tente novamente!")
                    else:
                        st.error("Certifique-se de que sua função esteja corretamente definida como 'calcular_fatorial_divisao'.")
                except Exception as e:
                    st.error(f"Erro ao executar o código: {e}")
        else:
            st.image(images[card_id]["front"], use_column_width=True)

# Adicionar seção de informações no rodapé
st.markdown("---")
st.write("**Desafio NEXT FIAP 2024**")
