import chromadb
from chromadb.utils import embedding_functions

CHROMA_DATA_PATH = "data/chromaDB/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "demo_docs"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"},
)

documents = [
    "The latest iPhone model comes with impressive features and a powerful camera.",
    "Exploring the beautiful beaches and vibrant culture of Bali is a dream for many travelers.",
    "Einstein's theory of relativity revolutionized our understanding of space and time.",
    "Traditional Italian pizza is famous for its thin crust, fresh ingredients, and wood-fired ovens.",
    "The American Revolution had a profound impact on the birth of the United States as a nation.",
    "Regular exercise and a balanced diet are essential for maintaining good physical health.",
    "Leonardo da Vinci's Mona Lisa is considered one of the most iconic paintings in art history.",
    "Climate change poses a significant threat to the planet's ecosystems and biodiversity.",
    "Startup companies often face challenges in securing funding and scaling their operations.",
    "Beethoven's Symphony No. 9 is celebrated for its powerful choral finale, 'Ode to Joy.'",
    "Toronto is a nice place.",
]

genres = [
    "technology",
    "travel",
    "science",
    "food",
    "history",
    "fitness",
    "art",
    "climate change",
    "business",
    "music",
    "country",
]

collection.add(
    documents=documents,
    ids=[f"id{i}" for i in range(len(documents))],
    metadatas=[{"genre": g} for g in genres]
)

if __name__ == '__main__':
    query_results = collection.query(
        query_texts=["Which food is the best?"],
        n_results=2,
    )

    print(f"1. {query_results}")
    print(f"2. {query_results.keys()}")
    print(f"3. {query_results['documents']}")
    print(f"4. {query_results['ids']}")
    print(f"5. {query_results['distances']}")
    print(f"6. {query_results['metadatas']}")
    
    # --- Perform a search using a query  ---
    q1 = "Find me some delicious food!"
    q2 = "I am looking to buy a new Phone."
    queries = [q1, q2]
    query_results = collection.query(
        query_texts=queries,
        n_results=2,  # Retrieve the top 2 results
    )

    # --- Print the results  ---
    for i, q in enumerate(queries):
        print(f'Query: {q}')
        print(f'Results:')
        for j, doc in enumerate(query_results['documents'][i]):
            print(f'{j+1}. {doc}')
        print('\n')