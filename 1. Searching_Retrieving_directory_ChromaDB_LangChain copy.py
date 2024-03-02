# import chromadb
from langchain_community.vectorstores import Chroma

# from chromadb.utils import embedding_functions
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

# loader = PyPDFLoader(file_path="./data/pdf/Python Programming - An Introduction To Computer Science.pdf")
# documents = loader.load()

directory = 'data/pets_txt/'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
print(len(documents))

# split into chunks
# text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
# docs = text_splitter.split_documents(documents=documents)

# split the docs into chunks using recursive character splitter
def split_docs(documents,chunk_size=1000,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

# store the splitte documnets in docs variable
docs = split_docs(documents)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load into chroma
db = Chroma.from_documents(documents=docs,embedding=embedding_function,)

query = "What are the emotional benefits of owning a pet?"
matching_docs = db.similarity_search(query)

print(matching_docs[0])


# query = "python gui"
# docs = db.similarity_search(query)

# # print(docs)
# print(docs[0].page_content)
# # print(docs[0].page_content.replace("\n", " "))