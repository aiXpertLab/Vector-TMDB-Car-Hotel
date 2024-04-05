# https://medium.com/@weidagang/hello-llm-demystifying-embeddings-and-vector-databases-61cd8df89dc5
# In the realm of artificial intelligence (AI), data representation plays a pivotal role. 
# Gone are the days when we relied solely on keywords and simple numerical data. 
# Today, the concept of embeddings is revolutionizing the way AI systems understand and process information. 
# Let’s explore the world of embeddings and how they lead us to the powerful concept of vector databases.

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="collection1_1")

collection.add(
    documents=["This is a document about engineer", "This is a document about steak"],
    metadatas=[{"source": "doc1"}, {"source": "doc2"}],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["Which food is the best?"],
    n_results=1
)

print(results)