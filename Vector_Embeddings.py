# from https://realpython.com/chromadb-vector-database/#practical-example-add-context-for-a-large-language-model-llm
import streamlit as st
from utils.st_def import st_main_contents, st_logo

st_logo(title='Welcome 👋 to Car Review!', page_title="Review Analysis",)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["🔰Saving ids", "➡️CSV", "🪻To Pinecon", "Embedding🍍", "Vector🎍", "Retrieval➡️", "Q&A➡️", "Evaluation🏅"])
st_main_contents()
