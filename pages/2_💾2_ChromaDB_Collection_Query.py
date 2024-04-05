# import sys, os
# if "STREAMLIT_SERVER_ENABLED" in os.environ and "IS_STREAMLIT_SERVER" in os.environ: __import__('pysqlite3'); sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from utils import st_def

import chromadb     #0.4.24
from   chromadb.utils import embedding_functions

st_def.st_logo(title='Welcome 👋 to Chroma DB!', page_title="Chroma DB ",)
st_def.st_load_book()
#-----------------------------------------------
EB_MODEL = "all-MiniLM-L6-v2"
COL_NAME = "collection2"

with st.spinner('Loading files...'):
    client = chromadb.Client()
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EB_MODEL)
    collection = client.get_or_create_collection(name=COL_NAME,  embedding_function=embedding_func,  metadata={"hnsw:space": "cosine"},)
    st.markdown("### Documents in Chroma DB")
    documents = [
        "The latest iPhone model comes with impressive features and a powerful camera.",
        "Exploring the beautiful beaches and vibrant culture of Bali is a dream for many travelers.",
        "Einstein's theory of relativity revolutionized our understanding of space and time.",
        "Traditional Italian pizza is famous for its thin crust, fresh ingredients, and wood-fired ovens.",
        "The American Revolution had a profound impact on the birth of the United States as a nation.",
        "Regular exercise and a balanced diet are essential for maintaining good physical health.",
        "Leonardo da Vinci's Mona Lisa is considered one of the most iconic paintings in art history.",
        "Climate change poses a significant threat to the planet's ecosystems and biodiversity.",
        "Startup companies often face challenges in securing funding and scaling their operations.",
        "Beethoven's Symphony No. 9 is celebrated for its powerful choral finale, 'Ode to Joy.'",
        "Toronto is a nice place.",
    ]
    genres = ["technology","travel","science","food","history","fitness",        "art","climate change","business","music","country",]
    collection.add(
        documents=documents,
        ids=[f"id{i}" for i in range(len(documents))],
        metadatas=[{"genre": g} for g in genres]
    )

for doc, genre in zip(documents, genres):
    st.write(f"{doc} ( {genre})")

# url = st.text_input('🌐 Ask questions about above: ')

if "msg1" not in st.session_state:      
    st.session_state.msg1 = []      #111
    st.session_state.msg1.append({"role": "system", 'content': "hi"})
    st.session_state.msg1.append({"role": "assistant",   "content": "How May I Help You Today💬?"})

for message in st.session_state.msg1[1:]:
    with st.chat_message(message["role"]):  st.markdown(message["content"])     #222

if prompt := st.chat_input("💬Ask me anything about the documents above!🍦"):
    with st.chat_message("user"):           st.markdown(prompt)
    st.session_state.msg1.append({"role": "user", "content": prompt})

    response = collection.query(query_texts=[f"{prompt}"],        n_results=2,)
    with st.chat_message("assistant"):          
        st.markdown(response['documents'][0][0])
        st.markdown(response['metadatas'][0][0]['genre'])
    st.session_state.msg1.append({"role": "assistant", "content": response['documents'][0][0]})