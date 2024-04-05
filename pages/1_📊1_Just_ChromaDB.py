__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st, sqlite3, chromadb
from streamlit import logger
from utils.st_def import st_logo, st_load_book

st_logo(title='Welcome 👋 to Chroma DB!', page_title="Chroma DB ",)
st_load_book()
#-----------------------------------------------
st.write(logger.get_logger("SMI_APP"))
st.write(f"{sys.version}")
st.header(f"sqlite version: {sqlite3.sqlite_version}")
#-----------------------------------------------
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="collection1_1")
collection.add(
    documents=["This is a document about engineer", "This is a document about steak"],
    metadatas=[{"source": "doc1"}, {"source": "doc2"}],
    ids=["id1", "id2"]
)
