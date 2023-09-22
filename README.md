# MentorGPT

## Introduction

Welcome to MentorGPT, an innovative application designed to help users extract information from PDF files and interact with a large language model like OpenAI's GPT-4.0. This README provides an overview of the application, its purpose, features, system design, and the technologies used in its development.

## Purpose

MentorGPT is created with the goal of simplifying the process of extracting relevant information from PDF documents and engaging in natural language conversations with the extracted content. Whether you're a researcher, student, or professional, MentorGPT can assist you in breaking down PDF files into text chunks and leveraging advanced language models like GPT-4.0 to gain insights and answers from the text.

## Features

### 1. PDF Text Extraction

MentorGPT allows users to upload PDF files, which are then processed to extract text content. This extracted text serves as the basis for subsequent interactions with the language model.

### 2. Integration with OpenAI's GPT-4.0

The application integrates seamlessly with OpenAI's GPT-4.0 model, enabling users to ask questions, seek explanations, or request summaries of the information extracted from the PDFs. The language model provides natural language responses to user queries.

### 3. Natural Language Interface

MentorGPT provides a user-friendly and intuitive natural language interface for interacting with the integrated language model. Users can simply type or speak their questions, and the application will generate coherent responses.

### 4. Vector Store Databases

The application employs vector store databases to efficiently store and retrieve information from the processed PDF documents. This technology ensures quick access to relevant information for user queries.

## System Design

![System Design Diagram](/systemdesign/MentorGPT.jpg)
## Mock up

![Project Mockup](/systemdesign/mockup.png)

## Technologies Used

MentorGPT is built using the following technologies:

- **Python**: The core programming language used for developing the application.
- **LangChain**: LangChain is a proprietary library that aids in natural language processing and facilitates interactions with OpenAI's GPT-4.0 model.
- **Vector Store Databases**: These databases are used to store and manage the extracted information from PDF files efficiently.
- **Hugging Face**: Hugging Face provides the state-of-the-art GPT-4.0 model and NLP libraries for seamless integration.


## Getting Started

To get started with MentorGPT, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies, including Python and LangChain.
3. Set up the necessary configurations, such as API keys for OpenAI integration.
4. Launch the application and start uploading PDF files for text extraction and querying.

## Usage

1. Upload PDF Files: Use the application's interface to upload one or more PDF files.
2. Extract Text: The application will extract text content from the uploaded PDFs.
3. Ask Questions: Enter your questions or queries in natural language.
4. Get Answers: The integrated GPT-4.0 model will generate responses based on the extracted text.

## Contributions

We welcome contributions from the open-source
