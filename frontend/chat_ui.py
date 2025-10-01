# Chat container, input bar, display functions
import streamlit as st

def display_chat(messages):
    chat_placeholder = st.container()
    with chat_placeholder:
        st.markdown('<div class="chat-container" id="chat-box">', unsafe_allow_html=True)
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            cls = "user-msg" if role=="user" else "agent-msg"
            st.markdown(f'<div class="message {cls}">{content}</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-end"></div></div>', unsafe_allow_html=True)
        st.markdown("""
        <script>
        var chatBox = document.getElementById('chat-box');
        if (chatBox) { chatBox.scrollTop = chatBox.scrollHeight; }
        </script>
        """, unsafe_allow_html=True)

def input_bar(key="chat_input"):
    container = st.container()
    with container:
        st.markdown('<div class="input-fixed">', unsafe_allow_html=True)
        cols = st.columns([8,1])
        query = cols[0].text_input("Enter your query", key=key, placeholder="Ask about financial news, trends, calculations, or summarize articles:", label_visibility="collapsed")
        submit_clicked = cols[1].button("Send")
        st.markdown('</div>', unsafe_allow_html=True)
    return query, submit_clicked
