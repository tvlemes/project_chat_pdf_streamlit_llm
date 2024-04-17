"""
App Chat com LLM, HuggingFace e Streamlit
Autor: Thiago Vilarinho Lemes
e-mail: contatothiagolemes@gmail.com
Data: 16/04/2024

OBS.: Não foi utilizado o Pinecone devido a instabilidade
da internet.
"""

from main import ChatBot
import streamlit as st

bot = ChatBot()

# Configurações da Página    
st.set_page_config(page_title="Bot do Thiago")
with st.sidebar:
    st.title('Bot Especiarias - Temperos \
             Autor: Thiago V. Lemes')

# Função para gerar resposta LLM
def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result

# Armazenar respostas geradas pelo LLM
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Bem vindo, eu sou o Assistente Virtual, como posso ajudá-lo?"}]

# Exibir mensagens de bate-papo
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Solicitação fornecida pelo usuário
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)
    response = bot.input_text(input)

# Gere uma nova resposta se a última mensagem não for do assistente
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Obtendo sua resposta..."):
            # response = generate_response(input) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)