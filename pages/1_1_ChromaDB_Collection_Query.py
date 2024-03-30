import streamlit as st
from utils import st_def, utilities

import chromadb     #0.4.24
from   chromadb.utils import embedding_functions

DB_PATH  = "data/chromaDB/"
EB_MODEL = "all-MiniLM-L6-v2"
COL_NAME = "pure_chroma_collection"

openai_api_key= st_def.st_sidebar()

with st.spinner('Loading files...'):

    # client = chromadb.PersistentClient(path=DB_PATH)
    client = chromadb.Client()
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EB_MODEL)
    collection = client.get_or_create_collection(
        name=COL_NAME,  embedding_function=embedding_func,  metadata={"hnsw:space": "cosine"},)
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
    genres = [
        "technology",
        "travel",
        "science",
        "food",
        "history",
        "fitness",
        "art",
        "climate change",
        "business",
        "music",
        "country",
    ]
    collection.add(
        documents=documents,
        ids=[f"id{i}" for i in range(len(documents))],
        metadatas=[{"genre": g} for g in genres]
    )

for doc, genre in zip(documents, genres):
    st.write(f"{doc} ( {genre})")

if "messages1" not in st.session_state:      
    st.session_state.messages1 = []      #111
    st.session_state.messages.append({"role": "system", 'content': "hi"})
    st.session_state.messages.append({"role": "assistant",   "content": "How May I Help You Today💬?"})

for message in st.session_state.messages1[1:]:
    with st.chat_message(message["role"]):  st.markdown(message["content"])     #222

if prompt := st.chat_input("💬Ask me anything about the documents above!🍦"):
    with st.chat_message("user"):           st.markdown(prompt)
    st.session_state.messages1.append({"role": "user", "content": prompt})

    response = collection.query(query_texts=[f"{prompt}"],        n_results=2,)
    with st.chat_message("assistant"):          
        st.markdown(response['documents'][0][0])
        st.markdown(response['metadatas'][0][0]['genre'])
    st.session_state.messages1.append({"role": "assistant", "content": response['documents'][0][0]})