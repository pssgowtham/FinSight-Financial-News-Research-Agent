# FAISS index creation & retrieval
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

INDEX_PATH = "faiss_index"

def create_vectorstore(docs):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(INDEX_PATH)
    return vectorstore

def load_vectorstore():
    if os.path.exists(INDEX_PATH):
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return None
