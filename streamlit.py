"""
App Chat com LLM, HuggingFace e Streamlit
Autor: Thiago Vilarinho Lemes
Data: 16/04/2024

OBS.: Não foi utilizado o Pinecone devido a instabilidade
da internet.
"""

from main import ChatBot
import streamlit as st

bot = ChatBot()
    
st.set_page_config(page_title="Bot do Thiago")
with st.sidebar:
    st.title('Bot Especiarias - Temperos \
             Autor: Thiago V. Lemes')

# Function for generating LLM response
def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Bem vindo, como posso ajudá-lo?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)
    response = bot.input_text(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Obtendo sua resposta..."):
            # response = generate_response(input) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)