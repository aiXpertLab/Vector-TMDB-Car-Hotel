import streamlit as st
from utils import st_def, car_data_etl

st_def.st_logo(title = "Welcome 👋 to Summary!", page_title="Summary",)
st_def.st_summary()
#------------------------------------------------------------------------     
def main():
    DATA_PATH = "data/archive/*"
    chroma_car_reviews_dict = car_data_etl.prepare_car_reviews_data(DATA_PATH)
    st.write(chroma_car_reviews_dict.keys())
    st.write(chroma_car_reviews_dict["ids"][-10])
    st.write(chroma_car_reviews_dict["documents"][-10])
    st.write(chroma_car_reviews_dict["metadatas"][-10])

if __name__ == "__main__":
    main()