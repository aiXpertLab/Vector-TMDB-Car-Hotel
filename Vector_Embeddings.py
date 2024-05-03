# from https://realpython.com/chromadb-vector-database/#practical-example-add-context-for-a-large-language-model-llm
import streamlit as st
from utils import st_def

st_def.st_mainpage(title='👋 Big Data Analysis!', page_title="Review Analysis",slogan='ChromaDB, Pinecone, other Vectors')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["🔰General", "➡️CSV", "🪻To Pinecon", "Embedding🍍", "Vector🎍", "Retrieval➡️", "Q&A➡️", "Evaluation🏅"])
with tab1:
    st.markdown('Vector databases extend the capabilities of traditional relational databases to embeddings.'
                'However, the key distinguishing feature of a vector database is that query results aren’t '
                'an exact match to the query. Instead, using a specified similarity metric, the vector '
                'database returns embeddings that are **`similar to a query`**.')
    st.subheader('Another awesome feature of ChromaDB: ')
    st.success('is the ability to filter queries on metadata.')

st.image('./images/zhang.gif')