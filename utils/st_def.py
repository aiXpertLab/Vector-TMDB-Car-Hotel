import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def st_sidebar():
    st.sidebar.image("data/sslogo.png", use_column_width=True)

    with st.sidebar:
        store_link = st.text_input("Enter Your Store URL:",   value="http://hypech.com/StoreSpark", disabled=True, key="store_link")
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        st.write("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        add_vertical_space(2)
        st.write('Made with ❤️ by [aiXpertLab](https://hypech.com)')

    return openai_api_key

def main_contents():
        main_contents="""

            ### 🚀 Bridge the Gap: Chatbots for Every Store 🍨

            Tired of missing out on sales due to limited customer support options? Struggling to keep up with growing customer inquiries? Store Spark empowers you to seamlessly integrate a powerful ChatGPT-powered chatbot into your website, revolutionizing your customer service and boosting engagement. No coding required! No modifications for current site needed!

            ### 📄Key Features📚:

            -  🔍 No Coding Required: Say goodbye to developer fees and lengthy website updates. Store Spark’s user-friendly API ensures a smooth integration process.

            -  📰 Empower Your Business: Offer instant customer support, improve lead generation, and boost conversion rates — all with minimal setup effort.

            -  🍨 Seamless Integration: Maintain your existing website design and user experience. Store Spark seamlessly blends in, providing a unified customer journey.


            """
        return main_contents