__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from streamlit import logger
import sqlite3

app_logger = logger.get_logger("SMI_APP")
app_logger.info(f"{sqlite3.sqlite_version}")
app_logger.info(f"{sys.version}")

st.write(logger.get_logger("SMI_APP"))
st.write(f"{sys.version}")
st.header(f"{sqlite3.sqlite_version}")