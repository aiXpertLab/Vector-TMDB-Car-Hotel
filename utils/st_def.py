
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def st_sidebar():
    # st.sidebar.image("data/images/sslogo.png", use_column_width=True)

    with st.sidebar:
        # store_link = st.text_input("Enter Your Store URL:",   value="http://hypech.com/StoreSpark", disabled=True, key="store_link")
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        st.write("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        add_vertical_space(2)
        st.write('Made with ❤️ by [aiXpertLab](https://hypech.com)')

    return openai_api_key

def st_main_contents():
        st.image("./data/images/zhang.gif")
        # main_contents="""
        #     ### 🚀 Bridge the Gap: Chatbots for Every Store 🍨
        #     Tired of missing out on sales due to limited customer support options? Struggling to keep up with growing customer inquiries? Store Spark empowers you to seamlessly integrate a powerful ChatGPT-powered chatbot into your website, revolutionizing your customer service and boosting engagement. No coding required! No modifications for current site needed!
        #     ### 📄Key Features📚:
        #     -  🔍 No Coding Required: Say goodbye to developer fees and lengthy website updates. Store Spark’s user-friendly API ensures a smooth integration process.
        #     -  📰 Empower Your Business: Offer instant customer support, improve lead generation, and boost conversion rates — all with minimal setup effort.
        #     -  🍨 Seamless Integration: Maintain your existing website design and user experience. Store Spark seamlessly blends in, providing a unified customer journey.
        #     """
    
def st_logo(title="aiXpert!", page_title="Aritificial Intelligence"):
    st.set_page_config(page_title,  page_icon="🚀",)
    st.title(title)

    st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {
            background-image: url(https://hypech.com/storespark/images/logohigh.png);
            background-repeat: no-repeat;
            padding-top: 80px;
            background-position: 15px 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def st_text_preprocessing_contents():
    st.markdown("""
        - Normalize Text
        - Remove Unicode Characters
        - Remove Stopwords
        - Perform Stemming and Lemmatization
    """)    


def st_create_collection():
    st.markdown("""
You then instantiate a PersistentClient() object, create the collection, and add data to the collection. In lines 29 to 39, you add data to the collection in batches using the more-itertools library. Calling batched(document_indices, 166) breaks document_indices into a list of tuples, each with size 166. ChromaDB’s current maximum batch size is 166, but this might change in the future.    """)    
    st.image("./data/images/book.png")

def st_summary():
    st.markdown("In your car_data_etl.py script, prepare_car_reviews_data() accepts the path to the car reviews dataset and a list of vehicle years to filter on, and it returns a dictionary with the review data properly formatted for ChromaDB. You can include different vehicle years, but keep in mind that the more years you include, the longer it’ll take to build the collection. By default, you’re only including vehicles from 2017.")
    st.markdown("In this block, you import prepare_car_reviews_data() from car_data_etl.py, store the path to the raw review CSV datasets, and create chroma_car_reviews_dict, which stores the reviews in a ChromaDB-compatible format. You then display the ID, document text, and metadata associated with one of the reviews.")
    # st.image("./data/images/featureengineering.png")

def st_case_study():
        st.image("./data/images/NLP-Pipeline.png")
        # main_contents="""
        #     ### 🚀 Bridge the Gap: Chatbots for Every Store 🍨
        #     Tired of missing out on sales due to limited customer support options? Struggling to keep up with growing customer inquiries? Store Spark empowers you to seamlessly integrate a powerful ChatGPT-powered chatbot into your website, revolutionizing your customer service and boosting engagement. No coding required! No modifications for current site needed!
        #     ### 📄Key Features📚:
        #     -  🔍 No Coding Required: Say goodbye to developer fees and lengthy website updates. Store Spark’s user-friendly API ensures a smooth integration process.
        #     -  📰 Empower Your Business: Offer instant customer support, improve lead generation, and boost conversion rates — all with minimal setup effort.
        #     -  🍨 Seamless Integration: Maintain your existing website design and user experience. Store Spark seamlessly blends in, providing a unified customer journey.
        #     """
    
