import streamlit as st
from utils import st_def, ut_vector, car_data_etl
import chromadb, os, json, openai
from chromadb.utils import embedding_functions

st_def.st_logo(title = "Welcome 👋 to AI Summary!", page_title="AI Summary",)
# st_def.st_ai_summary()
openai_api_key = st_def.st_sidebar()
client = openai.OpenAI(api_key = openai_api_key)
#------------------------------------------------------------------------
DATA_PATH = "data/archive/*"
CHROMA_PATH = "data/car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

client_db = chromadb.PersistentClient(CHROMA_PATH)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_FUNC_NAME)
collection = client_db.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
else: 
    context = """
    You are a customer success employee at a large
    car dealership. Use the following car reviews
    to answer questions: {}
    """

    question = """
    What's the key to great customer satisfaction
    based on detailed positive reviews?
    """

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