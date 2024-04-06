import sys, os
if "STREAMLIT_SERVER_ENABLED" in os.environ and "IS_STREAMLIT_SERVER" in os.environ: 
    print("server side")
    __import__('pysqlite3') 
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
else:
    import sqlite3

import streamlit as st
from streamlit import logger
from utils.st_def import st_logo, st_load_book
import chromadb

st_logo(title='Welcome 👋 to Chroma DB!', page_title="Chroma DB ",)
st_load_book()
#-----------------------------------------------
st.write(logger.get_logger("SMI_APP"))
# st.write(f"sys version: {sys.version}")
# st.header(f"sqlite version: {sqlite3.sqlite_version}")
#-----------------------------------------------
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="collection1_1")
collection.add(
    documents=["steak", "python", "tiktok", "safety", "health", "environment"],
    metadatas=[{"source": "food"}, {"source": "progamming language"}, {"source": "social media"}, {"source": "government"}, {"source": "body"}, {"source": "living condition"}],
    ids=["id1", "id2", "id3", "id4", "id5", "id6"]
)

qa = st.text_input('🌐 Ask the Chroma: ')
if qa:
    results = collection.query(query_texts=[qa],    n_results=1)
    st.write(results)


