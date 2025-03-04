import os
import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load API Key
load_dotenv()
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")

# Load LLM & Embeddings
llm = ChatNVIDIA(model_name="deepseek-ai/deepseek-r1")
embedding_model = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5")

# Streamlit UI
st.title("📄 PDF Chatbot with NVIDIA NIM & FAISS")
st.write("Upload a PDF and ask questions!")

# File Upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process the uploaded PDF
    loader = PyPDFDirectoryLoader("./")
    document = loader.load()

    # Split document
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", ";", ",", " ", ""],
    )
    document_chunks = text_splitter.split_documents(document)

    # Create FAISS vector store
    vector_store = FAISS.from_documents(document_chunks, embedding=embedding_model)

    # Display confirmation
    st.success("✅ PDF uploaded and processed successfully!")

    # User Query Input
    user_query = st.text_input("🔍 Ask a question about the document:")

    if user_query:
        # Define Prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", 
                "You are a helpful and friendly AI!"
                "Your responses should be concise and no longer than two sentences."
                "Do not hallucinate. Say you don't know if you don't have this information."
                "Answer the question using only the context."
                "\n\nQuestion:{question}\n\nContext:{context}"
            ),
            ("user", "{question}")
        ])

        # Create Query Chain
        chain = (
            {
                "context": vector_store.as_retriever(),
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        # Get Answer
        response = chain.invoke(user_query)

        # Display Answer
        st.subheader("🤖 AI Response:")
        st.write(response)
