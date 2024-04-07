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

with st.spinner('Building collection ...'):
    chroma_car_reviews_dict = car_data_etl.prepare_car_reviews_data(DATA_PATH)

    collection = ut_vector.car_review_collection(
        chroma_path = CHROMA_PATH,
        collection_name = COLLECTION_NAME,
        embedding_func_name = EMBEDDING_FUNC_NAME,
        ids = chroma_car_reviews_dict["ids"],
        documents=chroma_car_reviews_dict["documents"],
        metadatas=chroma_car_reviews_dict["metadatas"]
    )
    
st.write(collection.peek())