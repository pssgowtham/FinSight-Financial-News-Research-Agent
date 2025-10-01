# PlaywrightURLLoader + text splitting
from langchain_community.document_loaders import PlaywrightURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_urls(urls):
    loader = PlaywrightURLLoader(urls=[u for u in urls if u.strip()], headless=True)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(data)
    return docs
