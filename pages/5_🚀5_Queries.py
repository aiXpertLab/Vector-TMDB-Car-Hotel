import streamlit as st
from utils import st_def, ut_vector, car_data_etl

st_def.st_logo(title = "Welcome 👋 to Text Cleaning!", page_title="Text Cleaning",)
st_def.st_create_collection()
#------------------------------------------------------------------------
import chromadb
from chromadb.utils import embedding_functions

DATA_PATH = "data/archive/*"
CHROMA_PATH = "data/car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"

client = chromadb.PersistentClient(CHROMA_PATH)
with st.spinner('Building collection ...'):
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_FUNC_NAME)
    collection = client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

    great_reviews = collection.query(
        query_texts=["Find me some positive reviews that discuss the car's performance"],
        n_results=5,
        include=["documents", "distances", "metadatas"]
    )

    st.write(great_reviews["documents"][0])