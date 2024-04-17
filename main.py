"""
App Chat com LLM, HuggingFace e Streamlit
Autor: Thiago Vilarinho Lemes
e-mail: contatothiagolemes@gmail.com
Data: 16/04/2024

OBS.: Não foi utilizado o Pinecone devido a instabilidade
da internet.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import Pinecone
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_community.vectorstores import FAISS
import pinecone
# from pinecone import ServerlessSpec, PodSpec
# from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv

class ChatBot():

  # Pega as chaves da variável de ambiente do SO
  load_dotenv()

  ###################### Keys ################################################
  HUGGINGFACE_API_KEY = os.environ['HUGGINGFACE_API_KEY']
  # PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
  #############################################################################


  ###################### Splitter e Embedding do Arquivo ######################
  # Especifique o nome do conjunto de dados e a coluna que contém o arquivo utilizado
  dataset_path = "./spice_completo.pdf"

  loader = PyPDFLoader(dataset_path)
  documents = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
  docs = text_splitter.split_documents(documents)
  embeddings = HuggingFaceEmbeddings()

  # Defina o caminho para o modelo pré-treinado que você deseja usar
  modelPath = "sentence-transformers/all-MiniLM-l6-v2"

  # Cria um dicionário com opções de configuração do modelo, especificando o uso da CPU para cálculos
  model_kwargs = {'device':'cpu'}

  # Cria um dicionário com opções de codificação, definindo especificamente 'normalize_embeddings' como False
  encode_kwargs = {'normalize_embeddings': False}
  # Inicialize o cliente Pinecone

  # Inicialize uma instância de HuggingFaceEmbeddings com os parâmetros especificados
  embeddings = HuggingFaceEmbeddings(
      model_name=modelPath,     # Fornece o caminho do modelo pré-treinado
      model_kwargs=model_kwargs, # Passa as opções de configuração do modelo
      encode_kwargs=encode_kwargs # Passa as opções de codificação
  )

  # Faz o embeddings do texto
  db = FAISS.from_documents(docs, embeddings)
  #############################################################################


  #################### Armazenando no Pinecone ################################
  # pinecone = pinecone.Pinecone(api_key=PINECONE_API_KEY)

  # # Definir nome do índice
  # index_name = "chat-huggingface"

  # # Verificando índice
  # if index_name not in pinecone.list_indexes().names():
  #   # Criar novo índice
  #   pinecone.create_index(
  #     name=index_name,
  #     metric="cosine",
  #     dimension=768,
  #     # spec=ServerlessSpec(
  #     #   cloud='aws',    # Provedor de nuvem
  #     #   region='us-east-1'  # Região da nuvem
  #     # )
  #   )
  #   docsearch = Pinecone.from_documents(
  #     docs,
  #     embeddings,
  #     index_name=index_name
  #   )
  # else:
  #   # Link para o índice existente
  #   docsearch = Pinecone.from_existing_index(index_name, embeddings)

  # Defina o ID do repositório e conecte-se ao modelo Mixtral no Huggingface
  # repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
  #############################################################################

  ################ Chat #######################################################
  repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
  llm = HuggingFaceHub(
    repo_id=repo_id,
    model_kwargs={"temperature": 0.8, "top_k": 50},
    huggingfacehub_api_token=HUGGINGFACE_API_KEY
  )

  template = """
    You are a chef and you know about spices and seasonings. These Human will ask you a questions These humans will ask questions about spices and cooking seasonings..
    Use following piece of context to answer the question.
    If you don't know the answer, just say you don't know.
    Keep the answer within 2 sentences and concise.
    Context: {context}
    Question: {question}
    Answer:
  """

  prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
  )

  rag_chain = (
    {"context": db.as_retriever(),  "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
  )

  def input_text(self, qt):
  # user_input = input("Digite algo: ")
    searchDocs = self.rag_chain.invoke(qt)
    indice_answer = searchDocs.index("Answer:")

  # Extraindo a resposta
    answer = searchDocs[indice_answer + len("Answer:"):].strip()
    return answer
  
# while True:
#   bot = ChatBot()
#   input_question = input('Digite a sua pergunta: ')
#   resp = bot.input_text(input_question)
#   print(resp)