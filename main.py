
import streamlit as stream
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings,OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template


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
def get_conversation(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
def handle_input(question_input):
    response = stream.session_state.conversation({'question': question_input})

    stream.session_state.chat_history = response['chat_history']

    for i, message in enumerate(stream.session_state.chat_history):
        if i % 2 == 0:
            stream.write(user_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)
        else:
            stream.write(bot_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)

              

def main():
    #initialize .env
    load_dotenv()
    # Page configuration
    stream.set_page_config(page_title="Chat with the Mentor",page_icon=":books:")
    # initialize html
    stream.write(css, unsafe_allow_html=True)
    if "conversation" not in stream.session_state:
        stream.session_state.conversation = None
    if "chat_history" not in stream.session_state:
        stream.session_state.chat_history = None
    # Header section
    stream.header("Chat with your Mentor")
    # Handle user question input
    question_input = stream.text_input("Ask a question to the Mentor")
    if question_input:
        handle_input(question_input)

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
                # create a conversation chain
                stream.session_state.conversation = get_conversation(vectorstore)



if __name__ == "__main__":
    main()