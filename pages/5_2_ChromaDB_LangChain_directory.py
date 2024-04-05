from langchain_community.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

import streamlit as st, os 
from utils import st_def, utilities
openai_api_key = st_def.st_sidebar()

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents


with st.spinner('Loading files...'):
  documents = load_docs('data/pets_txt/')
  file_names = [os.path.basename(doc.metadata['source']) for doc in documents]
  st.write('\n\n'.join(file_names))

  def split_docs(documents,chunk_size=1000,chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

  docs = split_docs(documents)

  embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

  db = Chroma.from_documents(documents=docs,embedding=embedding_function,)

  if "messages2" not in st.session_state:      
      st.session_state.messages2 = []      #111
      st.session_state.messages2.append({"role": "system", 'content': "hi"})
      st.session_state.messages2.append({"role": "assistant",   "content": "How May I Help You Today💬?"})

  for message in st.session_state.messages2[1:]:
      with st.chat_message(message["role"]):  st.markdown(message["content"])     #222

if prompt := st.chat_input("💬Ask me anything about the documents above!🍦"):
    with st.chat_message("user"):           st.markdown(prompt)
    st.session_state.messages2.append({"role": "user", "content": prompt})

    matching_docs = db.similarity_search(prompt)
    with st.chat_message("assistant"):          
        st.markdown(matching_docs[0].page_content)
    st.session_state.messages2.append({"role": "assistant", "content": matching_docs[0].page_content})

# query = "What are the emotional benefits of owning a pet?"
