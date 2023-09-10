
import streamlit as stream
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings,OpenAIEmbeddings
from langchain.vectorstores import FAISS


def get_plain_text(pdf_documents):
    text = ""
    for pdf in pdf_documents:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
# Below references can be found here: https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/character_text_splitter
def get_chunks_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
# Embeddings
def get_vectorstore(chunks_text):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=chunks_text, embedding=embeddings)
    return vectorstore
def main():
    #initialize .env
    load_dotenv()
    # Page configuration
    stream.set_page_config(page_title="Chat with the Mentor",page_icon=":books:")
    # Header section
    stream.header("Chat with your Mentor")
    stream.text_input("Ask a question to the Mentor")
    # Side bar section
    with stream.sidebar:
        stream.subheader("Documents")
        pdf_documents = stream.file_uploader("Upload The PDFs here and click on Process", accept_multiple_files=True)
        if stream.button("Process"):
            with stream.spinner("Processing"):
                #There are 3 parts of the process
                # extract the text from PDF file
                plain_text = get_plain_text(pdf_documents)
                # Get the text into chunks
                chunks_text = get_chunks_text(plain_text)
                # create the vector store for the text chunks
                vectorstore = get_vectorstore(chunks_text)



if __name__ == "__main__":
    main()