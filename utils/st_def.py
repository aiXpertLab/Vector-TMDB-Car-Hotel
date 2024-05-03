import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


def st_sidebar():

    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        st.write("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        add_vertical_space(2)
        st.write('Made with ❤️ by [aiXpertLab](https://hypech.com)')

    return openai_api_key


def st_logo(title="OmniExtract!", page_title="Aritificial Intelligence", slogan=""):
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>",unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>{slogan}</h2>",unsafe_allow_html=True)
    st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {
            background-image: url(https://hypech.com/images/logo/aixpertlab_logo.png);
            background-size: 300px; /* Set the width and height of the image */
            background-repeat: no-repeat;
            padding-top: 40px;
            background-position: 1px 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def st_mainpage(title="OmniExtract!", page_title="Aritificial Intelligence", slogan=""):
    st.set_page_config(page_title,  page_icon="🚀",)
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>",unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>{slogan}</h2>",unsafe_allow_html=True)
    st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {
            background-image: url(https://hypech.com/images/logo/aixpertlab_logo.png);
            background-size: 300px; /* Set the width and height of the image */
            background-repeat: no-repeat;
            padding-top: 40px;
            background-position: 1px 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


