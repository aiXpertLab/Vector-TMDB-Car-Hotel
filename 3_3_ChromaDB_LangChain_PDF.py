import streamlit as st
from utils import st_def, utilities
openai_api_key= st_def.st_sidebar()

from langchain_community.vectorstores import Chroma

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

pdf = st.file_uploader('Upload your PDF Document', type='pdf')

if pdf is not None:

    with st.spinner('Loading files...'):

        loader = PyPDFLoader(file_path="./data/pdf/Python Programming - An Introduction To Computer Science.pdf")
        documents = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
        docs = text_splitter.split_documents(documents=documents)
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        db = Chroma.from_documents(documents=docs,
                                embedding=embedding_function,collection_name="basic_langchain_chroma",)

        query = "python gui"
        docs = db.similarity_search(query)

    st.text(docs[0].page_content)