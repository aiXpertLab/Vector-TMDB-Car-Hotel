import torch, sys
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM

from langchain_community.llms       import LlamaCpp, CTransformers
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_community.embeddings import LlamaCppEmbeddings, HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma, FAISS
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader, WebBaseLoader, PyPDFDirectoryLoader, CSVLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.prompts       import PromptTemplate
from langchain.chains        import LLMChain, RetrievalQA

# data = load_dataset("HuggingFaceTB/cosmopedia", "stories", split="train")

# data = data.to_pandas()
# data.to_csv("e:/E:/models/huggingface.cache/HuggingFaceTB___cosmopedia/stories/dataset.csv")
# data.head()

loader = CSVLoader(file_path='E:/models/huggingface.cache/HuggingFaceTB___cosmopedia/stories/dataset.csv')
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
docs = text_splitter.split_documents(data)

modelPath = "sentence-transformers/all-MiniLM-l6-v2"
model_kwargs = {'device':'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceEmbeddings(
 model_name=modelPath, 
 model_kwargs=model_kwargs, 
 encode_kwargs=encode_kwargs 
)

# db = FAISS.from_documents(docs, embeddings)
