# Main Streamlit entrypoint
import streamlit as st
from backend import config, urls_processor, vectorstore, llm_agent
from frontend import chat_ui, styles

# Setup environment and NLTK
config.setup_environment()

st.set_page_config(page_title="FinSight Agent", page_icon="🤖", layout="wide")
st.title("🤖 FinSight: Financial News Agent with Sources")
st.caption("Ask questions, summarize articles, do calculations, or search for news.")
st.markdown(styles.STYLES, unsafe_allow_html=True)

# Sidebar URL inputs
st.sidebar.header("🔗 News Sources")
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url_clicked = st.sidebar.button("Process URLs")

# Session storage for docs and messages
if "processed_docs" not in st.session_state: st.session_state.processed_docs = []
if "messages" not in st.session_state: st.session_state.messages = []

# Process URLs
if process_url_clicked:
    with st.spinner("Loading articles..."):
        docs = urls_processor.process_urls(urls)
        if docs:
            vectorstore.create_vectorstore(docs)
            st.session_state.processed_docs = docs
            st.success(f"✅ Processed {len(docs)} document chunks")
        else:
            st.error("❌ No valid documents found.")

# Load vectorstore & init agent
vs = vectorstore.load_vectorstore()
agent = llm_agent.init_agent(processed_docs=st.session_state.processed_docs, vectorstore=vs)

# Display chat
chat_ui.display_chat(st.session_state.messages)

# Input bar
query, submit_clicked = chat_ui.input_bar()

# Handle user input
if submit_clicked and query:
    st.session_state.messages.append({"role":"user","content":query})
    chat_ui.display_chat(st.session_state.messages)
    spinner = st.empty()
    with spinner:
        st.markdown('<div class="spinner-container">🤖 Thinking...</div>', unsafe_allow_html=True)
        try:
            response = agent.invoke({"input": query})["output"]
            st.session_state.messages.append({"role":"assistant","content":response})
        except Exception as e:
            st.session_state.messages.append({"role":"assistant","content":f"❌ Error: {e}"})
    spinner.empty()
    chat_ui.display_chat(st.session_state.messages)
