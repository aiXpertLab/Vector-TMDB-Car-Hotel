import sys, os, platform

if not platform.processor()[:7]=="Intel64":
  __import__('pysqlite3'); 
  sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
  print(f'server-------------------  {platform.processor()}')
else:
  print(f'local-------------------  {platform.processor()}')


import sqlite3, chromadb

def chroma_collection(name):
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name=name)
    return collection



