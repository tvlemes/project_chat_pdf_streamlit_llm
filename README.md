# Projeto Chat com Hugging Face

<img src="https://github.com/tvlemes/project_database_openai/blob/main/docs/print.PNG"> 

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Indície</summary>
  <ol>
    <li>
      <a href="#objetivo">Objetivo</a>
      <ul>
        <li><a href="#bibliotecas-utilizadas">Bibliotecas utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#arquivos">Arquivos</a>
    </li>
    <li>
      <a href="#rodando-o-projeto">Rodando o projeto</a>
    </li>
    <li>
      <a href="#sobre">Sobre</a>
    </li>
  </ol>
</details>

## Objetivo

Este projeto tem como objetivo criar um <b>Chatbot</b> com <b>LLM</b> e <b>Hugging Face</b>, biblioteca de IA Generativa, para interagir com arquivos PDF. No atual projeto o arquivo que está sendo utilizado é setado no código fonte em <b>main.py</b>, este arquivo possui o nome <b>spice_completo.pdf</b>

<b>OBS.: não foi utilizado um Banco de Dados vetorial devido a instabilidade na internet, por isso foi utilizado o FAISS do Facebook local.</b>

<!-- programas-e-bibliotecas -->
### Bibliotecas utilizadas

Nele foi implementado as seguintes bibliotecas:

* langchain==0.1.6
* langchain_community==0.0.19
* langchain_core==0.1.23
* pinecone-client==2.2.4
* python-dotenv==1.0.0
* streamlit==1.29.0

<!-- arquivos-e-pastas -->
## Arquivos

A estrutura física contém o arquivo <b>main.py</b> que é o arquivo da estrutura funcional do <b>LLM</b> e <b>Hugging Face</b>. 

O arquivo <b>streamlit.py</b> contém a estrura da página Web para interação.

No arquivo requirements.txt são as dependências do projeto, as bibliotecas.

Para que o projeto possa rodar é preciso renomear o arquivo <b>.env_example</b> para <b>.env</b> e inserir as chaves nele descrito.

<!-- rodando-o-projeto -->
## Rodando o projeto

Para rodar o projeto dentro do diretório raiz no prompt digite:
```
streamlit run streamlit.py
``` 
<!-- sobre -->
## Sobre

Autor: Thiago Vilarinho Lemes <br>
LinkedIn <a href="https://www.linkedin.com/in/thiago-v-lemes-b1232727">Thiago V. Lemes</a><br>
e-mail: contatothiagolemes@gmail.com | lemes_vilarinho@yahoo.com.br



