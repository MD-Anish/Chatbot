import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables (for API key)
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Streamlit UI
st.title("🚀 Groq-Powered Chatbot")
st.caption("A fast AI chatbot powered by Groq (Llama 3 70B)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get Groq's response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # Or "mixtral-8x7b-32768"
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=2048,
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    # Add assistant reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})