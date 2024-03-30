import streamlit as st
from utils.utilities import get_products, aichat
from utils.st_def import st_sidebar, main_contents

st.set_page_config(page_title="Store Spark: Chatbots for Every Store",  page_icon="🚀",)
st.title("Welcome 👋 to Store Spark!")
st.markdown(main_contents())

openai_api_key = st_sidebar()
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-0125"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system",
                                      'content': f"""
            You are ShopBot, an AI assistant for my online fashion shop. 

            Your role is to assist customers in browsing products, providing information, and guiding them through the checkout process. 

            Be friendly and helpful in your interactions.

            We offer a variety of products across categories such as Women's Clothing, Men's clothing, Accessories, Kids' Collection, Footwears and Activewear products. 

            Feel free to ask customers about their preferences, recommend products, and inform them about any ongoing promotions.

            The Current Product List is limited as below:

            ```{get_products()}```

            Make the shopping experience enjoyable and encourage customers to reach out if they have any questions or need assistance.
            """})
    st.session_state.messages.append({"role": "assistant",   "content": "How May I Help You Today💬?"})


# Display chat messages from history on app rerun
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("💬Looking for tees, drinkware, headgear, bag, accessories, or office supplies?🍦Ask me!"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    else: 
        try:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                stream = aichat(messages = [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],openai_api_key=openai_api_key)
                response = st.write_stream(stream)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.info("Invalid OpenAI API key. Please enter a valid key to proceed.")