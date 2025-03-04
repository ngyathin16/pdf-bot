# imports
import time
import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# code
load_dotenv()
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")

# load the LLM NIM by specifying the model name
llm=ChatNVIDIA(model_name="deepseek-ai/deepseek-r1")

# Initialize and connect to a NeMo Retriever Text Embedding NIM (nvidia/nv-embedqa-e5-v5) 
embedding_model = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5")

# Load the PDFs from your data folder in your project
loader = PyPDFDirectoryLoader("./data")
document = loader.load()

# Split the documents using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=900,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", ";", ",", " ", ""],
)

document_chunks = text_splitter.split_documents(document)

# Create FAISS vector store from documents using the NIM Embedding model
vector_store = FAISS.from_documents(document_chunks, embedding=embedding_model)

prompt = ChatPromptTemplate.from_messages([
    ("system", 
        "You are a helpful and friendly AI!"
        "Your responses should be concise and no longer than two sentences."
        "Do not hallucinate. Say you don't know if you don't have this information."
        "Answer the question using only the context"
        "\n\nQuestion:{question}\n\nContext:{context}"
    ),
    ("user", "{question}")
])

chain = (
    {
        "context": vector_store.as_retriever(),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

print(chain.invoke("what are the benefits?"))