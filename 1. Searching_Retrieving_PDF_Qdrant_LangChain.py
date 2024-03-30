import asyncio

from langchain_community.vectorstores import Qdrant
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader(file_path="./data/pdf/Python Programming - An Introduction To Computer Science.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
docs = text_splitter.split_documents(documents=documents)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load into chroma
async def asynchronous_vectore_store(docs, embedding_function) -> None:
    db = Qdrant.from_documents(docs, embedding_function,  location=":memory:")
    query = "What is the long form of http"
    docs = await db.asimilarity_search(query)
    print(docs[0].page_content.replace("\n", " "))


asyncio.run(asynchronous_vectore_store(
    docs=docs, embedding_function=embedding_function))