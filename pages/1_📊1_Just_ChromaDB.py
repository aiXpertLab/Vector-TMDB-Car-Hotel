import streamlit as st, platform
from streamlit import logger
from utils import st_def, ut_vector

st_def.st_logo(title='Welcome 👋 to Chroma DB!', page_title="Chroma DB ",)
st_def.st_load_book()
st.write(platform.processor())
st.write(logger.get_logger("SMI_APP"))
#-----------------------------------------------
collection = ut_vector.chroma_collection(name="collection1_1")
collection.add(
    documents=["steak", "python", "tiktok", "safety", "health", "environment"],
    metadatas=[{"source": "food"}, {"source": "progamming language"}, {"source": "social media"}, {"source": "government"}, {"source": "body"}, {"source": "living condition"}],
    ids=["id1", "id2", "id3", "id4", "id5", "id6"]
)

qa = st.text_input('🌐 Ask the Chroma: ')
if qa:
    results = collection.query(query_texts=[qa],    n_results=1)
    st.write(results)


