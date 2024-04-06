import sys, os

# __import__('pysqlite3') 
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import sqlite3
import chromadb

def chroma_collection(name):
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name=name)
    return collection
