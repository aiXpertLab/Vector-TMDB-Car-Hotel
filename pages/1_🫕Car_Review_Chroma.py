import streamlit as st, openai, os
from streamlit_extras.stateful_button import button
from utils import st_def, car, ut_vector

st_def.st_logo(title = "Welcome 👋 to Summary!", page_title="Summary",)
tab1, tab2, tab3, tab4= st.tabs(["🔰from csv to Dictionary", "➡️Build Collection🎍", "🪻Query based on Chroma Only", "🍍OpenAI Summary"])
#------------------------------------------------------------------------
import chromadb
from chromadb.utils import embedding_functions

DATA_PATH   = "./data/car_review/*"
CHROMA_PATH = "./data/car_review_chroma"
EMBEDDING_FUNC = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME= "car_review_collection"
#------------------------------------------------------------------------
with tab1:  #read from csv, import to Dictionary
    car.st_summary()
    if button("csv 2 Dictonary", key="button2"):
        chroma_car_reviews_dict = car.prepare_car_reviews_data(DATA_PATH)   # return a dictionary with review1, review2
        st.write(chroma_car_reviews_dict.keys())
#------------------------------------------------------------------------
with tab2:  # Create Chroma Collection
    if button("Build Collection", key="button1"):
        with st.spinner('Building collection ...'):
            collection = ut_vector.car_review_collection(
                chroma_path=CHROMA_PATH,
                collection_name=COLLECTION_NAME,
                embedding_func_name=EMBEDDING_FUNC,
                ids=chroma_car_reviews_dict["ids"],
                documents=chroma_car_reviews_dict["documents"],
                metadatas=chroma_car_reviews_dict["metadatas"]
            )

        st.write(collection.peek())

with tab3:
    client_db = chromadb.PersistentClient(CHROMA_PATH)
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_FUNC)
    collection = client_db.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

    query=["Find me some positive reviews that discuss the car's performance"],
    st.text(query)
    great_reviews = collection.query(
        query_texts=[f"{query}"],
        n_results=10,
        include=["documents", "distances", "metadatas"]
    )

    st.write(len(great_reviews))
    st.write(great_reviews["documents"][0])

with tab4:
    if button("AI?", key="button4"):
        openai_api_key = st_def.st_sidebar()
        client = openai.OpenAI(api_key=openai_api_key)
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
        else:
            context = """You are a customer success employee at a large car dealership. Use the following car reviews to answer questions: {}"""

            question = """What's the key to great customer satisfaction based on detailed positive reviews?"""

            good_reviews = collection.query(
                query_texts=[question],
                n_results=10,
                include=["documents"],
                where={"Rating": {"$gte": 3}},
            )

            reviews_str = ",".join(good_reviews["documents"][0])

            good_review_summaries = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": context.format(reviews_str)},
                    {"role": "user", "content": question},
                ],
                temperature=0,
                n=1,
            )

            st.write(good_review_summaries.choices[0].message.content)