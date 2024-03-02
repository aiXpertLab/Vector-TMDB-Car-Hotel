# import chromadb
from langchain_community.vectorstores import Chroma

# from chromadb.utils import embedding_functions
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

loader = PyPDFLoader(file_path="./data/pdf/Python Programming - An Introduction To Computer Science.pdf")
documents = loader.load()

# split into chunks
text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
docs = text_splitter.split_documents(documents=documents)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load into chroma
db = Chroma.from_documents(documents=docs,
                           embedding=embedding_function,
                           collection_name="basic_langchain_chroma",
                           persist_directory="data/chromaDBLangChain"
                           )

query = "python gui"
docs = db.similarity_search(query)

# print(docs)
print(docs[0].page_content)
# print(docs[0].page_content.replace("\n", " "))