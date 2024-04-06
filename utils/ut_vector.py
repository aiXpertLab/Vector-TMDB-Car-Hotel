import sys, os
import sqlite3
import chromadb

def chroma_collection(name):
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name=name)
    return collection



# import sys, os, platform
# import streamlit as st

# print(platform.processor()[:7]=="Intel64")

# if not platform.processor()[:7]=="Intel64":
#   __import__('pysqlite3'); 
#   sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# else:
#   st.write('local')
