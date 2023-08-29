#import streamlit
import streamlit as stream

def main():
    # Page configuration
    stream.set_page_config(page_title="Chat with the Mentor",page_icon=":books")
    # Header section
    stream.header("Chat with your Mentor")
    stream.text_input("Ask a question to the Mentor")
    # Side bar section
    with stream.sidebar:
        stream.subheader("Documents")
        stream.file_uploader("Upload The PDFs here and click on Process")
        stream.button("Process")
if __name__ == "__main__":
    main()