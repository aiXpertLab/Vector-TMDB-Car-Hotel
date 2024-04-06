from utils.util_doc_processing import DocProcessing
from langchain_community.vectorstores import Chroma

from langchain_openai import ChatOpenAI
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.chains.question_answering import load_qa_chain

documents = DocProcessing.load_directory('data/pets_txt/')

docs = DocProcessing.split_docs(documents) # store the splitte documnets in docs variable

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(documents=docs,embedding=embedding_function,)    # load into chroma

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

chain = load_qa_chain(llm, chain_type="stuff",verbose=True)

query = "What are the emotional benefits of owning a pet?"
matching_docs = db.similarity_search(query)

answer =  chain.run(input_documents=matching_docs, question=query)
print(answer)