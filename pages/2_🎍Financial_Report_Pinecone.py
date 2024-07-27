import streamlit as st, os, time, csv, pickle, pandas as pd, json, pinecone
from streamlit_extras.stateful_button import button
from utils import st_def, tmdb, mypinecone

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader, WebBaseLoader, PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_community.embeddings import LlamaCppEmbeddings, HuggingFaceEmbeddings


st_def.st_logo(title='🎥 Financial Report', page_title="👋 Pinecone!", slogan='The better way to analyze financial report')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PINECONE_ENV  = os.environ.get('PINECONE_ENV')
OPENAI_API_KEY  = os.environ.get('OPENAI_API_KEY')
PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔰Loading PDFs", "➡️Split to Chunk", "🍍Save to Pinecone", "🪻Pinecon",  "Query🎍", "ChatGPT🏅"])

with tab1:
    try:
        if 'docs' not in st.session_state:
            if button("Loading PDF", key="button1"):
                loader = DirectoryLoader(path='./data/google/', glob="*.pdf", loader_cls=PyPDFLoader, show_progress=True)
                docs = loader.load()
                st.session_state['docs'] = docs
        else:
            docs = st.session_state['docs']
        st.write(docs)
        st.text(len(docs))
    except Exception as e:
        print(e)

with tab2:
    if button("Split to Chunk", key="button2"):
        text_splitter = CharacterTextSplitter(            chunk_size=1000,            chunk_overlap=0        )
        docs_split = text_splitter.split_documents(docs)
        st.write(docs_split)

with tab3:
    if button("Combine CSV", key="button3"):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})
        doc_db = PineconeVectorStore.from_documents(
            docs_split,
            embeddings,
            index_name='d384'
        )


with tab4:
    st.write(pc.list_indexes())
    index = pc.Index("d384")
    #BE CAREFUL:  delete_response = index.delete(delete_all=True)

with tab5:
    query = st.text_input("query")
    if query:
        search_docs = doc_db.similarity_search(query)
        st.write(search_docs)