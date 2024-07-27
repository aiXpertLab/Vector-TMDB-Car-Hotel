import streamlit as st, os, pickle
from PyPDF2 import PdfReader

from langchain_community.callbacks.manager  import get_openai_callback
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings         import HuggingFaceEmbeddings

from langchain_openai                    import OpenAI, OpenAIEmbeddings
from langchain.text_splitter             import RecursiveCharacterTextSplitter, TextSplitter
from langchain.chains.question_answering import load_qa_chain

from utils import st_def

st.set_page_config(page_title='🤗💬 PDF Chat App - GPT')
st.title('🦜🔗 Ask PDF')
openai_api_key= st_def.st_sidebar()
GPT_MODEL = "gpt-3.5-turbo-instruct"
EB_MODEL = "text-embedding-3-small"

def main():
    st.header("Talk to your PDF 💬")
    st.write("This app uses OpenAI's LLM model to answer questions about your PDF file. Upload your PDF file and ask questions about it. The app will return the answer from your PDF file.")

    st.header("1. Upload PDF")
    pdf = st.file_uploader("**Upload your PDF**", type='pdf')

    if not openai_api_key:
        st.info("⬅️Please add your OpenAI API key to continue.")
    elif pdf is not None:
        try:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:            text += page.extract_text()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,            chunk_overlap=200,            length_function=len)
            chunks = text_splitter.split_text(text=text)

            store_name = pdf.name[:-4]
            st.write(f'{store_name}')

            if os.path.exists(f"{store_name}.pkl"):
                with open(f"{store_name}.pkl", "rb") as f:
                    VectorStore = pickle.load(f)
            else: 
                # embeddings = OpenAIEmbeddings(model=EB_MODEL)
                embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
                VectorStore = FAISS.from_texts(chunks, embedding=embeddings)

            st.header("2. Ask questions about your PDF file:")
            q="Tell me about the content of the PDF"
            query = st.text_input("Questions",value=q)

            if st.button("Ask"):
                docs = VectorStore.similarity_search(query=query, k=3)

                llm = OpenAI(model=GPT_MODEL)
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=query)
                    print(cb)
                st.header("Answer:")
                st.write(response)
                st.write('--')
                st.header("OpenAI API Usage:")
                st.text(cb)
        except Exception as generic_error:
            st.info("An unexpected error occurred:", generic_error)

if __name__ == '__main__':
    main()
